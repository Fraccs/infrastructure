# homelab/docker-compose

> 🐙 Docker Compose deployments in my `homelab`.

## Useful information

### Interpolation of `docker-compose.yml` files

Some `docker-compose.yml` require interpolation. To achieve that, place the variables that have to be interpolated in a `.env` file.

### Environment variables

Each stack that uses environment variables contains a `.template.env` file (or `.template.<service>.env` in case of multiple services in the stack) with some configuration values set by default. Secrets are defaulted to a blank string. When deploying make sure to fill the empty secrets.

The following one-liner can help you rename the `.template.*env` files to `*.env`:

```sh
find . -type f -name '.template.*env' -exec sh -c 'mv $1 "$(echo "$1" | sed 's/\.template//')"' _ "{}" \;
```

## Deployments

### deb-01

| Stack | Container Name | Container Image | Host Port | Internal Port | Network |
| ----- |----------------|-----------------|-----------|---------------| ------- |
| node-exporter | node-exporter | [prom/node-exporter:latest](https://hub.docker.com/r/prom/node-exporter) | 9100 | 9100 | auto |
| portainer-agent | portainer-agent | [portainer/agent:latest](https://hub.docker.com/r/portainer/agent) | 9001 | 9001 | auto |
| watchtower | watchtower | [containrrr/watchtower:latest](https://hub.docker.com/r/containrrr/watchtower/tags) | 10220 | 8080 | auto |

### ubt-01

| Stack | Container Name | Container Image | Host Port | Internal Port | Network |
| ----- |----------------|-----------------|-----------|---------------| ------- |
| node-exporter | node-exporter | [prom/node-exporter:latest](https://hub.docker.com/r/prom/node-exporter) | 9100 | 9100 | auto |
| pihole | pihole | [pihole/pihole:latest](https://hub.docker.com/r/pihole/pihole) | 53,10150 | 53,80 | auto |
| portainer-agent | portainer-agent | [portainer/agent:latest](https://hub.docker.com/r/portainer/agent) | 9001 | 9001 | auto |
| romm | romm | [zurdi15/romm:latest](https://hub.docker.com/r/zurdi15/romm) | 10172 | 8080 | auto |
| romm | romm-mariadb | [mariadb:latest](https://hub.docker.com/_/mariadb) | / | 3306 | auto |
| watchtower | watchtower | [containrrr/watchtower:latest](https://hub.docker.com/r/containrrr/watchtower/tags) | 10220 | 8080 | auto |

### ubt-02

| Stack | Container Name | Container Image | Host Port | Internal Port | Network |
| ----- |----------------|-----------------|-----------|---------------| ------- |
| firefly | firefly | [fireflyiii/core:latest](https://hub.docker.com/r/fireflyiii/core) | 10050 | 8080 | auto |
| firefly | firefly-cron | [alpine:latest](https://hub.docker.com/_/alpine) | / | / | auto |
| firefly | firefly-mariadb | [mariadb:latest](https://hub.docker.com/_/mariadb) | / | 3306 | auto |
| nextcloud | nextcloud | [nextcloud:latest](https://hub.docker.com/_/nextcloud/) | 10130 | 80 | auto |
| nextcloud | nextcloud-mariadb | [mariadb:latest](https://hub.docker.com/_/mariadb) | / | 3306 | auto |
| node-exporter | node-exporter | [prom/node-exporter:latest](https://hub.docker.com/r/prom/node-exporter) | 9100 | 9100 | auto |
| photoprism | photoprism | [photoprism/photoprism:latest](https://hub.docker.com/r/photoprism/photoprism) | 10157 | 2342 | auto |
| photoprism | photoprism-mariadb | [mariadb:latest](https://hub.docker.com/_/mariadb) | / | 3306 | auto |
| portainer-agent | portainer-agent | [portainer/agent:latest](https://hub.docker.com/r/portainer/agent) | 9001 | 9001 | auto |
| watchtower | watchtower | [containrrr/watchtower:latest](https://hub.docker.com/r/containrrr/watchtower/tags) | 10220 | 8080 | auto |

### ubt-03

| Stack | Container Name | Container Image | Host Port | Internal Port | Network |
| ----- |----------------|-----------------|-----------|---------------| ------- |
| ghostfolio | ghostfolio | [ghostfolio/ghostfolio:latest](https://hub.docker.com/r/ghostfolio/ghostfolio) | 3333 | 3333 | auto |
| ghostfolio | ghostfolio-postgres | [postgres:15](https://hub.docker.com/_/postgres) | / | 5432 | auto |
| ghostfolio | ghostfolio-redis | [redis:alpine](https://hub.docker.com/_/redis) | / | 6379 | auto |
| node-exporter | node-exporter | [prom/node-exporter:latest](https://hub.docker.com/r/prom/node-exporter) | 9100 | 9100 | auto |
| portainer-agent | portainer-agent | [portainer/agent:latest](https://hub.docker.com/r/portainer/agent) | 9001 | 9001 | auto |
| watchtower | watchtower | [containrrr/watchtower:latest](https://hub.docker.com/r/containrrr/watchtower/tags) | 10220 | 8080 | auto |
