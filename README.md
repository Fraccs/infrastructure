# docker-compose `main-server`

> 🐋 docker-compose deployments on `main-server`.

| Container Name | Container Image | Host Port | Internal Port |
|----------------|-----------------|-----------|---------------|
| barsempione49 | [httpd:2.4-bullseye](https://hub.docker.com/_/httpd) | 10010 | 80 |
| grafana | [grafana/grafana-oss:latest](https://hub.docker.com/r/grafana/grafana-oss) | 10060 | 3000 |
| homeassistant  | [lscr.io/linuxserver/homeassistant:latest](https://hub.docker.com/r/linuxserver/homeassistant) | 10070 | 8123 |
| homepage | [ghcr.io/benphelps/homepage:latest](https://github.com/benphelps/homepage/pkgs/container/homepage) | 10071 | 3000 |
| jackett | [linuxserver/jackett:latest](https://hub.docker.com/r/linuxserver/jackett) | 10090 | 9117 |
| jellyfin | [jellyfin/jellyfin:latest](https://hub.docker.com/r/jellyfin/jellyfin) | 10091 | 8096 |
| muse | [codetheweb/muse:latest](https://hub.docker.com/r/codetheweb/muse) | / | / |
| nextcloud | [nextcloud:latest](https://hub.docker.com/_/nextcloud/) | 10130 | 80 |
| nextcloud-mariadb | [mariadb:latest](https://hub.docker.com/_/mariadb) | / | 3306 |
| onlyoffice-documentserver | [onlyoffice/documentserver:latest](https://hub.docker.com/r/onlyoffice/documentserver) | 10140 | 80 |
| portainer | [portainer/portainer-ce:latest](https://hub.docker.com/r/portainer/portainer-ce) | 10150,10151 | 8000,9443 |
| portfolio | [ghcr.io/fraccs/portfolio:latest](https://github.com/Fraccs/portfolio/pkgs/container/portfolio) | 10152 | 80 |
| prometheus | [prom/prometheus:latest](https://hub.docker.com/r/prom/prometheus) | 10153 | 9090 |
| prometheus-node-exporter | [prom/node-exporter:latest](https://hub.docker.com/r/prom/node-exporter) | / | 9100 |
| qbittorrent | [linuxserver/qbittorrent:latest](https://hub.docker.com/r/linuxserver/qbittorrent) | 10160,10161/tcp,10161/udp | 10160,6881/tcp,6881/udp |
| radarr | [linuxserver/radarr:latest](https://hub.docker.com/r/linuxserver/radarr) | 10170 | 7878 |
| sonarr | [linuxserver/sonarr:latest](https://hub.docker.com/r/linuxserver/sonarr) | 10180 | 8989 |
| syncthing | [lscr.io/linuxserver/syncthing:latest](https://hub.docker.com/r/linuxserver/syncthing) | 10181,10182/udp,10183/tcp,10183/udp | 8384,21027/udp,22000/tcp,22000/udp |
| uptime-kuma | [louislam/uptime-kuma:latest](https://hub.docker.com/r/louislam/uptime-kuma) | 10200 | 3001 |
| watchtower | [containrrr/watchtower:latest](https://hub.docker.com/r/containrrr/watchtower/tags) | / | / |
