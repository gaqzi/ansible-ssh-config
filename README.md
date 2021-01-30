ansible-ssh-config
==================

THIS MODULE HAS MIGRATED TO https://github.com/ansible-collections/community.general/blob/main/plugins/modules/system/ssh_config.py
Use the community version instead.

A module for Ansible for configuring ssh configuration files.

# Why?

We have several libraries that carry shared functionality between
projects at work. These libraries are on GitHub and they're in their
own repo. Our deploy users don't have access to every single repo but
only the ones they need to deploy a specific project.

To manage this we have added in fake hostnames to our ~/.ssh/config
files on the line of:

```
Host: internal-lib.github.com
  Hostname: github.com
  IdentityFile: id_rsa.internal-lib
```

When I started out with Ansible I tried just adding in our lines
with [lineinfile], but it didn't work out for me since several lines
needed to be added.

# Usage

The usage is fairly straightforward and it handles the normal use
cases of adding, changing and removing hosts from your config file.

```yaml
- name: Add internal-lib.github.com to ssh config
  ssh_config: host=internal-lib.github.com hostname=github.com
              identity_file=id_rsa.internal-lib port=222 state=present
- name: Remove old-internal-lib.github.com from ssh config
  ssh_config: host=old-internal-lib.github.com state=absent
```

For the full set of options please look at the top of the module file.

# Installation

**Note**: The module needs to be installed into your library folder for
Ansible to pick it up.

## Requirements file

Add the following line to your `requirements.yml`:

```yaml
- src: gaqzi.ssh-config
  path: library/
```

## Ansible Galaxy
Alternatively install it from [Ansible Galaxy] by doing:

```shell
$ ansible-galaxy install gaqzi.ssh-config -p library/
```

Your directory structure should then look like this:

```
.
├── library
│   └── gaqzi.ssh-config
│       ├── CHANGELOG.md
│       ├── library
│       │   └── ssh_config.py
│       ├── meta
│       │   └── main.yml
│       └── README.md
└── site.yml
```

## Manual
Copy `ssh_config` into the library directory at the root of your Playbook.

```
.
├── library
│   └── ssh_config
└── site.yml
```

# Credits

For managing the config files I blatantly copied `ConfigParser`
from [stormssh] and [paramiko] which implemented all the functionality,
but since I want to keep everything in one file to be easily
reusable/shareable with Ansible we ended up here.

[lineinfile]: http://www.ansibleworks.com/docs/modules.html#lineinfile
[stormssh]: https://github.com/emre/storm/
[paramiko]: https://github.com/paramiko/paramiko
[Ansible Galaxy]: https://galaxy.ansible.com/
