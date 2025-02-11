# homelab/ansible

> 🕹️ Ansible automation in my `homelab`.

> [!WARNING]
> Work in progress! Expect changes and things not working as they should!

## Introduction

> This ansible project aims to be **completely idempotent**, this means that you could run the master playbook a million times, at any time, and the state of the infrastructure wouldn't change.

- The `site.yml` master playbook updates the infrastructure to match the state defined in this repository.

- Individual playbooks can be executed to perform single operations (*example: you only need to update your servers*).

## Useful commands

> Ansible is configured to automatically pick-up the inventory file and automatically ask for the vault password, there is no need to explicitly set command-line flags.
>
> The following commands are relative to the `homelab/ansible` directory.

```sh
pwd # .../homelab/ansible/
```

### Ping every device in the homelab group

```sh
ansible -m ping homelab
```

### Run a playbook

```sh
ansible-playbook <path_to_playbook>
```

### Edit the contents of a vault

```sh
ansible-vault edit <path_to_vault>
```
