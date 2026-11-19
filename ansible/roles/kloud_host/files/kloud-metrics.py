#!/usr/bin/python3
"""Bounded, read-only host checks; writes only the node-exporter textfile."""
import datetime
import json
import os
from pathlib import Path
import subprocess
import time

DESTINATION = Path('/var/lib/node_exporter/textfile_collector/kloud.prom')


def command(argv, timeout=10):
    try:
        return subprocess.run(argv, capture_output=True, text=True, timeout=timeout, check=False)
    except (OSError, subprocess.TimeoutExpired):
        return None


def collect():
    metrics = [f'kloud_host_probe_timestamp_seconds {time.time():.0f}']
    for unit in ('k3s', 'chrony', 'iscsid', 'kloud-firewall', 'wg-quick@wg-kore', 'kloud-video-proxy'):
        result = command(['systemctl', 'is-active', unit], timeout=3)
        active = int(result is not None and result.returncode == 0)
        metrics.append(f'kloud_systemd_active{{unit={json.dumps(unit)}}} {active}')
    for family in ('4', '6'):
        result = command(['curl', f'-{family}', '--head', '--silent', '--fail',
                          '--max-time', '8', 'https://www.debian.org/'], timeout=9)
        metrics.append(f'kloud_external_connectivity{{ip_family="{family}"}} '
                       f'{int(result is not None and result.returncode == 0)}')
    result = command(['/usr/local/bin/k3s', 'kubectl', 'get', '--raw=/readyz'], timeout=10)
    metrics.append(f'kloud_apiserver_ready {int(result is not None and result.returncode == 0)}')
    snapshots = Path('/var/lib/rancher/k3s/server/db/snapshots')
    newest = max((p.stat().st_mtime for p in snapshots.glob('*') if p.is_file()), default=0)
    metrics.append(f'kloud_etcd_snapshot_timestamp_seconds {newest:.0f}')
    result = command(['wg', 'show', 'wg-kore', 'latest-handshakes'], timeout=3)
    handshake = 0
    if result is not None and result.returncode == 0:
        handshake = max((int(line.split()[-1]) for line in result.stdout.splitlines() if line.split()), default=0)
    metrics.append(f'kloud_wireguard_handshake_timestamp_seconds {handshake}')
    for path in sorted(Path('/etc/kloud/pki-public').glob('*.pem')):
        result = command(['openssl', 'x509', '-in', str(path), '-noout', '-enddate'], timeout=3)
        if result is not None and result.returncode == 0:
            value = result.stdout.strip().split('=', 1)[1]
            expiry = datetime.datetime.strptime(value, '%b %d %H:%M:%S %Y %Z').replace(tzinfo=datetime.timezone.utc).timestamp()
            metrics.append(f'kloud_pki_certificate_not_after_seconds{{certificate={json.dumps(path.stem)}}} {expiry:.0f}')
    count = sum(line.startswith('kloud_pki_certificate_not_after_seconds{') for line in metrics)
    metrics.append(f'kloud_pki_public_material_total {count}')
    return '\n'.join(metrics) + '\n'


if __name__ == '__main__':
    temporary = DESTINATION.with_suffix('.prom.tmp')
    temporary.write_text(collect())
    temporary.chmod(0o644)
    os.replace(temporary, DESTINATION)
