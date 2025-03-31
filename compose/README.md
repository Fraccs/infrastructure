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

*Currently I run everything on Kubernetes, any future compose deployment will be listed here.*
