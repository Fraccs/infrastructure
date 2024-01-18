# homelab

>  🏡 The centralized, single source of truth, configuration repository for my `homelab`.

## Useful information

### Interpolation of `docker-compose.yml` files

Some `docker-compose.yml` require interpolation. To achieve that, place the variables that have to be interpolated in a `.env` file.

### Environment variables

Each stack that uses environment variables contains a `.template.env` file (or `.template.<service>.env` in case of multiple services in the stack) with some configuration values set by default. Secrets are defaulted to a blank string. When deploying make sure to fill the empty secrets.

When cloning the repository for the first time, rename the `.template.*env` files to `*.env` with the following command:

```sh
find . -type f -name '.template.*env' -exec sh -c 'mv $1 "$(echo "$1" | sed 's/\.template//')"' _ "{}" \;
```

## Deployments

| Stack | Container Name | Container Image | Host Port | Internal Port | Network |
| ----- |----------------|-----------------|-----------|---------------| ------- |
| authelia | authelia | [authelia/authelia:latest](https://hub.docker.com/r/authelia/authelia) | 10000 | 9091 | 172.16.0.0/24 |
| firefly | firefly | [fireflyiii/core:latest](https://hub.docker.com/r/fireflyiii/core) | 10050 | 8080 | 172.16.1.0/24 |
| firefly | firefly-cron | [alpine:latest](https://hub.docker.com/_/alpine) | / | / | 172.16.1.0/24 |
| firefly | firefly-mariadb | [mariadb:latest](https://hub.docker.com/_/mariadb) | / | 3306 | 172.16.1.0/24 |
| grafana | grafana | [grafana/grafana-oss:latest](https://hub.docker.com/r/grafana/grafana-oss) | 10060 | 3000 | 172.16.2.0/24 |
| homeassistant | homeassistant  | [linuxserver/homeassistant:latest](https://hub.docker.com/r/linuxserver/homeassistant) | 10070 | 8123 | 172.16.3.0/24 |
| homepage | homepage | [ghcr.io/benphelps/homepage:latest](https://github.com/benphelps/homepage/pkgs/container/homepage) | 10071 | 3000 | 172.16.4.0/24 |
| jellyfin | jellyfin | [jellyfin/jellyfin:latest](https://hub.docker.com/r/jellyfin/jellyfin) | 10090 | 8096 | 172.16.5.0/24 |
| muse | muse | [codetheweb/muse:latest](https://hub.docker.com/r/codetheweb/muse) | / | / | 172.16.6.0/24 |
| nextcloud | nextcloud | [nextcloud:latest](https://hub.docker.com/_/nextcloud/) | 10130 | 80 | 172.16.7.0/24 |
| nextcloud | nextcloud-mariadb | [mariadb:latest](https://hub.docker.com/_/mariadb) | / | 3306 | 172.16.7.0/24 |
| nginx-proxy-manager | nginx-proxy-manager | [jc21:nginx-proxy-manager:latest](https://hub.docker.com/r/jc21/nginx-proxy-manager) | 10131,10132,10133 | 80,81,443 | 172.16.8.0/24 |
| photoprism | photoprism | [photoprism/photoprism:latest](https://hub.docker.com/r/photoprism/photoprism) | 10157 | 2342 | 172.16.9.0/24 |
| photoprism | photoprism-mariadb | [mariadb:latest](https://hub.docker.com/_/mariadb) | / | 3306 | 172.16.9.0/24 |
| pihole | pihole | [pihole/pihole:latest](https://hub.docker.com/r/pihole/pihole) | 53,10150 | 53,80 | 172.16.10.0/24 |
| portainer | portainer | [portainer/portainer-ce:latest](https://hub.docker.com/r/portainer/portainer-ce) | 10151 | 9443 | 172.16.11.0/24 |
| portfolio | portfolio | [ghcr.io/fraccs/portfolio:latest](https://github.com/Fraccs/portfolio/pkgs/container/portfolio) | 10152 | 80 | 172.16.12.0/24 |
| portfolio | portfolio-api | [ghcr.io/fraccs/portfolio-api:latest](https://github.com/Fraccs/portfolio-api/pkgs/container/portfolio-api) | 10153 | 5174 | 172.16.12.0/24 |
| prometheus | prometheus | [prom/prometheus:latest](https://hub.docker.com/r/prom/prometheus) | 10154 | 9090 | 172.16.13.0/24 |
| prometheus | prometheus-node-exporter | [prom/node-exporter:latest](https://hub.docker.com/r/prom/node-exporter) | / | 9100 | 172.16.13.0/24 |
| romm | romm | [zurdi15/romm:latest](https://hub.docker.com/r/zurdi15/romm) | 10172 | 8080 | 172.16.14.0/24 |
| romm | romm-mariadb | [mariadb:latest](https://hub.docker.com/_/mariadb) | / | 3306 | 172.16.14.0/24 |
| samba | samba | [dperson/samba:latest](https://hub.docker.com/r/dperson/samba) | 139,445 | 139,445 | 172.16.15.0/24 |
| syncthing | syncthing | [linuxserver/syncthing:latest](https://hub.docker.com/r/linuxserver/syncthing) | 10181,10182/udp,10183/tcp,10183/udp | 8384,21027/udp,22000/tcp,22000/udp | 172.16.16.0/24 |
| vpn-routed | lidarr | [linuxserver/lidarr:latest](https://hub.docker.com/r/linuxserver/lidarr) | 10110 | 8686 | 172.16.17.0/24 |
| vpn-routed | protonvpn | [linuxserver/wireguard:latest](https://hub.docker.com/r/linuxserver/wireguard) | / | / | 172.16.17.0/24 |
| vpn-routed | prowlarr | [linuxserver/prowlarr:latest](https://hub.docker.com/r/linuxserver/prowlarr) | 10156 | 9696 | 172.16.17.0/24 |
| vpn-routed | qbittorrent | [linuxserver/qbittorrent:latest](https://hub.docker.com/r/linuxserver/qbittorrent) | 10160,10161/tcp,10161/udp | 10160,6881/tcp,6881/udp | 172.16.17.0/24 |
| vpn-routed | radarr | [linuxserver/radarr:latest](https://hub.docker.com/r/linuxserver/radarr) | 10170 | 7878 | 172.16.17.0/24 |
| vpn-routed | readarr | [linuxserver/readarr:nightly](https://hub.docker.com/r/linuxserver/readarr) | 10171 | 8787 | 172.16.17.0/24 |
| vpn-routed | sonarr | [linuxserver/sonarr:latest](https://hub.docker.com/r/linuxserver/sonarr) | 10180 | 8989 | 172.16.17.0/24 |
| watchtower | watchtower | [containrrr/watchtower:latest](https://hub.docker.com/r/containrrr/watchtower/tags) | 10220 | 8080 | 172.16.18.0/24 |
