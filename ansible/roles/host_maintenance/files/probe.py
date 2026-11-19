#!/usr/bin/env python3
"""Read-only maintenance gates; uses local root CLI access, never exports credentials."""
import argparse
import glob
import ipaddress
import json
from pathlib import Path
import re
import shlex
import socket
import subprocess
import time


def command(argv):
    result = subprocess.run(argv, text=True, capture_output=True, timeout=120,
                            env={"PATH": "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
                                 "LC_ALL": "C", "DEBIAN_FRONTEND": "noninteractive"})
    if result.returncode:
        raise ValueError(f"{argv[0]} failed: {result.stdout} {result.stderr}")
    return result.stdout


def require(condition, message):
    if not condition:
        raise ValueError(message)


def source_suites(text, deb822=False):
    if not deb822:
        suites = []
        for line in text.splitlines():
            line = line.split('#', 1)[0].strip()
            if re.match(r'^deb(?:-src)?\s', line):
                line = re.sub(r'\[[^]]*\]', '', line)
                fields = line.split()
                require(len(fields) >= 3, 'Malformed APT source')
                suites.append(fields[2])
        return suites
    suites = []
    for paragraph in re.split(r'\n\s*\n', text):
        fields = {}
        key = None
        for line in paragraph.splitlines():
            if not line.strip() or line.lstrip().startswith('#'):
                continue
            if line[0].isspace() and key:
                fields[key] += ' ' + line.strip()
            else:
                key, value = line.split(':', 1)
                key = key.lower()
                fields[key] = value.strip()
        if fields and fields.get('enabled', 'yes').lower() != 'no':
            require('suites' in fields, 'Missing Suites in enabled APT source')
            suites.extend(fields['suites'].split())
    return suites


def validate_suites(suites, codename):
    allowed = {codename, codename + '-updates', codename + '-security', codename + '-backports'}
    require(bool(suites) and set(suites) <= allowed,
            f'APT sources must stay on {codename}; found {suites}. Review third-party suites separately.')


def package_changes(output, pve_major):
    require(not re.search(r'^Remv ', output, re.M), 'Package removals require a reviewed manual transaction')
    changes = []
    for line in output.splitlines():
        if not line.startswith('Inst '):
            continue
        match = re.match(r'Inst (\S+)(?: \[([^]]+)\])? \((\S+)', line)
        require(match is not None, f'Unrecognized APT transaction: {line}')
        name, old, new = match.groups()
        if name.split(':')[0] in {'proxmox-ve', 'pve-manager'}:
            require(new.split(':')[-1].split('.')[0] == pve_major,
                    f'Refusing Proxmox major change: {old} -> {new}')
        changes.append({'package': name, 'installed': old, 'candidate': new})
    return changes


def packages(args):
    release = dict(line.split('=', 1) for line in Path('/etc/os-release').read_text().splitlines()
                   if '=' in line)
    release = {key: shlex.split(value)[0] for key, value in release.items() if value}
    require(release.get('ID') == 'debian' and release.get('VERSION_ID') == args.debian_major
            and release.get('VERSION_CODENAME') == args.codename, 'Unexpected Debian release')
    # Avoid the apt module installing its own dependencies before the drain.
    command(['/usr/bin/python3', '-c', 'import apt'])
    suites = []
    for name in ['/etc/apt/sources.list'] + glob.glob('/etc/apt/sources.list.d/*.list') + glob.glob('/etc/apt/sources.list.d/*.sources'):
        path = Path(name)
        if path.exists():
            suites.extend(source_suites(path.read_text(), path.suffix == '.sources'))
    validate_suites(suites, args.codename)
    require(not command(['dpkg', '--audit']).strip(), 'dpkg reports unfinished package configuration')
    if args.pve_major != 'none':
        version = command(['dpkg-query', '-W', '-f=${Version}', 'pve-manager']).strip()
        require(version.split(':')[-1].split('.')[0] == args.pve_major, 'Unexpected installed PVE major')
    output = command(['apt-get', '--simulate', '--no-remove', 'dist-upgrade'])
    return {'changes': package_changes(output, args.pve_major),
            'reboot_required': Path('/var/run/reboot-required').exists(),
            'debian': release['VERSION_ID'], 'codename': args.codename}


def validate_nodes(nodes, members, allowed_cordon):
    require({node['metadata']['name'] for node in nodes} == set(members),
            'Live Kubernetes membership differs from inventory')
    for node in nodes:
        name = node['metadata']['name']
        conditions = {c['type']: c['status'] for c in node.get('status', {}).get('conditions', [])}
        require(conditions.get('Ready') == 'True', f'{name} is not Ready')
        require(all(conditions.get(c, 'False') == 'False'
                    for c in ['MemoryPressure', 'DiskPressure', 'PIDPressure', 'NetworkUnavailable']),
                f'{name} has resource/network pressure')
        require(not node.get('spec', {}).get('unschedulable') or name == allowed_cordon,
                f'{name} was already cordoned; investigate before proceeding')


def validate_volumes(volumes):
    for volume in volumes:
        status = volume.get('status', {})
        require(status.get('robustness') == 'healthy' or
                (status.get('state') == 'detached' and status.get('robustness') == 'unknown'),
                f"Longhorn volume {volume['metadata']['name']} is not healthy")


def k3s(args):
    prefix = ['/usr/local/bin/k3s', 'kubectl', '--request-timeout=30s']
    command(prefix + ['get', '--raw=/readyz'])
    nodes = json.loads(command(prefix + ['get', 'nodes', '-o', 'json']))['items']
    validate_nodes(nodes, args.members.split(','), args.allowed_cordon)
    local_ips = {ipaddress.ip_address(a['local']) for i in json.loads(command(['ip', '-j', 'address']))
                 for a in i.get('addr_info', [])}
    target = next(node for node in nodes if node['metadata']['name'] == args.node)
    target_ips = {ipaddress.ip_address(a['address']) for a in target['status'].get('addresses', [])
                  if a['type'] == 'InternalIP'}
    require(bool(local_ips & target_ips), 'Requested Kubernetes node is not this SSH host')
    if not args.recovering:
        pods = json.loads(command(prefix + ['get', 'pods', '-A', '-o', 'json']))['items']
        for pod in pods:
            if pod.get('status', {}).get('phase') in {'Succeeded', 'Failed'}:
                continue
            require(not pod['metadata'].get('deletionTimestamp') and
                    any(c['type'] == 'Ready' and c['status'] == 'True'
                        for c in pod.get('status', {}).get('conditions', [])),
                    f"Pod not Ready: {pod['metadata']['namespace']}/{pod['metadata']['name']}")
        volumes = json.loads(command(prefix + ['get', 'volumes.longhorn.io', '-n', 'longhorn-system', '-o', 'json']))['items']
        validate_volumes(volumes)
    return {'healthy': True}


def validate_pve(status, members):
    clusters = [entry for entry in status if entry.get('type') == 'cluster']
    nodes = [entry for entry in status if entry.get('type') == 'node']
    require(len(clusters) == 1 and clusters[0].get('quorate') == 1, 'Proxmox has no quorum')
    require({entry['name'] for entry in nodes} == set(members) and
            all(entry.get('online') == 1 for entry in nodes), 'All expected Proxmox nodes must be online')


def validate_ha(ha, members, node, allowed_cordon, evacuated, now):
    master = [entry for entry in ha if entry.get('type') == 'master']
    lrms = [entry for entry in ha if entry.get('type') == 'lrm']
    require(len(master) == 1 and {entry.get('node') for entry in lrms} == set(members),
            'Incomplete HA manager/LRM status')
    require(all(-2 <= now - entry.get('timestamp', 0) < 60 for entry in master + lrms),
            'HA status is stale or clocks disagree')
    require(not any(entry.get('type') == 'fencing' and entry.get('armed-state') in {'disarmed', 'disarming'}
                    for entry in ha), 'HA fencing is disabled')
    require(all(entry.get('crm_state') in {'started', 'stopped', 'disabled', 'ignored'}
                for entry in ha if entry.get('type') == 'service'), 'HA services are failed or still transitioning')
    require(not any('(maintenance' in entry.get('status', '') and entry.get('node') != allowed_cordon
                    for entry in lrms), 'Another Proxmox node is already in maintenance')
    if evacuated:
        require(any(entry.get('node') == node and '(maintenance' in entry.get('status', '') for entry in lrms),
                'HA maintenance is not yet active')


def validate_evacuated(guests, node):
    require(not any(g.get('node') == node and g.get('status') != 'stopped' for g in guests),
            'Guests remain on this host (including non-HA guests); refusing package changes/reboot')


def proxmox(args):
    require(socket.gethostname().split('.')[0] == args.node, 'Requested PVE node is not this SSH host')
    status = json.loads(command(['pvesh', 'get', '/cluster/status', '--output-format', 'json']))
    validate_pve(status, args.members.split(','))
    command(['systemctl', 'is-active', 'pve-cluster', 'corosync', 'pvedaemon', 'pveproxy'])
    ha = json.loads(command(['pvesh', 'get', '/cluster/ha/status/current', '--output-format', 'json']))
    validate_ha(ha, args.members.split(','), args.node, args.allowed_cordon, args.evacuated, time.time())
    guests = json.loads(command(['pvesh', 'get', '/cluster/resources', '--type', 'vm', '--output-format', 'json']))
    if args.evacuated:
        validate_evacuated(guests, args.node)
    return {'healthy': True}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('mode', choices=['packages', 'k3s', 'proxmox'])
    parser.add_argument('--codename')
    parser.add_argument('--debian-major')
    parser.add_argument('--pve-major', default='none')
    parser.add_argument('--members', default='')
    parser.add_argument('--node', default='')
    parser.add_argument('--allowed-cordon', default='')
    parser.add_argument('--evacuated', action='store_true')
    parser.add_argument('--recovering', action='store_true')
    args = parser.parse_args()
    try:
        print(json.dumps(globals()[args.mode](args), sort_keys=True))
    except (ValueError, KeyError, OSError, subprocess.TimeoutExpired, StopIteration) as error:
        parser.exit(1, str(error) + '\n')


if __name__ == '__main__':
    main()
