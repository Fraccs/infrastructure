# homelab/compose

> 🐙 Compose stacks in my `homelab`.

## Useful information

### Interpolation of `compose.yml` files

Some `compose.yml` files require interpolation. To achieve that, place the variables that have to be interpolated in a `.env` file.

### Environment variables

Each stack that uses environment variables contains a `.template.env` file (or `.template.<service>.env` in case of multiple services in the stack) with some configuration values set by default. Secrets are defaulted to a blank string. When deploying make sure to fill the empty secrets.

The following one-liner can help you rename the `.template.*env` files to `*.env`:

```sh
find . -type f -name '.template.*env' -exec sh -c 'mv $1 "$(echo "$1" | sed 's/\.template//')"' _ "{}" \;
```

## Stacks

### deb-04

| Stack Name | Container Name | Container Image | Image Version | Image SHA256 Digest | Host Port | Internal Port |
| ----- | -------------- | --------------- | ------------- | ------------------- | --------- | ------------- |
| duplicati | duplicati | [docker.io/duplicati/duplicati](https://hub.docker.com/r/duplicati/duplicati) | `2.0.8.1_beta_2024-05-07` | `0ffff717b1465022c436afa409291c44fb55c601f7ad556b76db6932f3afbdcf` | 8200 | 8200 |
| mariadb | mariadb | [docker.io/library/mariadb](https://hub.docker.com/_/mariadb) | `11.5.2` | `baef228246e0bc50fe89b857db989ffe66020a651add05c3933366687b73100c` | 3306 | 3306 |
| node-exporter | node-exporter | [docker.io/prom/node-exporter](https://hub.docker.com/r/prom/node-exporter) | `v1.8.2` | `065914c03336590ebed517e7df38520f0efb44465fde4123c3f6b7328f5a9396` | 9100 | 9100 |
| redis | redis | [docker.io/library/redis](https://hub.docker.com/_/redis) | `7.4.1` | `1b5978db511770e4b8e3b06219d59be28281220f5ffa3fb93482087fdfd60624` | 6379 | 6379 |
