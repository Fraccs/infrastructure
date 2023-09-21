# docker-compose `main-server`

> 🐋 docker-compose deployments on `main-server`.

| Container Name | Container Image | Host Port | Internal Port |
|----------------|-----------------|-----------|---------------|
| barsempione49 | [httpd:2.4-bullseye](https://hub.docker.com/_/httpd) | 10010 | 80 |
| grafana | [grafana/grafana-oss:latest](https://hub.docker.com/r/grafana/grafana-oss) | 10060 | 3000 |
| homeassistant  | [lscr.io/linuxserver/homeassistant:latest](https://hub.docker.com/r/linuxserver/homeassistant) | 10070 | 8123 |
| muse | [codetheweb/muse:latest](https://hub.docker.com/r/codetheweb/muse) | / | / |
| portainer | [portainer/portainer-ce:latest](https://hub.docker.com/r/portainer/portainer-ce) | 10150,10151 | 8000,9443 |
| portfolio | [ghcr.io/fraccs/portfolio:latest](https://github.com/Fraccs/portfolio/pkgs/container/portfolio) | 10152 | 80 |
| prometheus | [prom/prometheus:latest](https://hub.docker.com/r/prom/prometheus) | 10153 | 9090 |
| node-exporter | [prom/node-exporter:latest](https://hub.docker.com/r/prom/node-exporter) | / | 9100 |
| syncthing | [lscr.io/linuxserver/syncthing:latest](https://hub.docker.com/r/linuxserver/syncthing) | 10180,10181/udp,10182/tcp,10182/udp | 8384,21027/udp,22000/tcp,22000/udp |
| watchtower | [containrrr/watchtower:latest](https://hub.docker.com/r/containrrr/watchtower/tags) | / | / |
