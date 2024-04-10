# homelab/ansible

> 🕹️ Ansible automation in my `homelab`.

Commands in this document are relative to the `homelab/ansible` directory.

```sh
pwd # /home/fraccs/Repos/homelab/ansible
```

## Common commands

### Ping all the devices in homelab

```sh
ansible homelab -m ping -i inventory.yml -J
```

### Run a playbook

```sh
ansible-playbook -i inventory.yml <path_to_playbook> -J
```

