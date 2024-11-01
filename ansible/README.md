# homelab/ansible

> 🕹️ Ansible automation in my `homelab`.

Commands in this document are relative to the `homelab/ansible` directory.

```sh
pwd # /home/fraccs/Repos/homelab/ansible
```

## Useful commands

### Ping all the devices in homelab

```sh
ansible homelab -m ping -i inventory.yml --ask-vault-pass
```

### Run a playbook

```sh
ansible-playbook -i inventory.yml <path_to_playbook> --ask-vault-pass
```

### Edit the contents of a vault

```sh
ansible-vault edit <path_to_vault>
```
