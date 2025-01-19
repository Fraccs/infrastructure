nfs_exports_apply
=========

Overrides `/etc/exports` on the target node with a locally provided `exports` file and applies the nfs exports.

*p.s. This role is so stupidly trivial that it probably shouldn't even be a role.*

Requirements
------------

- The local nfs `exports` file to be applied.

*I suggest to place the `exports` file in a `files` directory adjacent to the playbook (example directory: `ansible/playbooks/nfs_exports_apply/files/exports`).*

Role Variables
--------------

| Variable | Description | Type | Required |
| -------- | ----------- | ---- | -------- |
| `nfs_exports_file_path` | The path to the `exports` file | `string` | `true` |

Dependencies
------------

This role has no extra dependencies.

Example Playbook
----------------

```yaml
---
- name: Apply NFS exports
  hosts: my_nfs_server
  become: true
  roles:
    - nfs_exports_apply
  vars:
    nfs_exports_file_path: "{{ playbook_dir }}/files/exports"
```

License
-------

MIT

Author Information
------------------

- It's me.
