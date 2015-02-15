# Change Log

## [0.1.0] - 2015-02-15
### Added
- Remove options that are not present in host definition.
  E.g. if the `user` option is set in the config file and is not
  set in ansible then it will be removed on the nextansible run.
  (@z38 on GitHub)
- Allow the config file for the root user to be set.
  Previous versions assumed that the default user was root and that the
  config file was `/etc/ssh/ssh_config`.

  It has now been changed so that
  if the user is unset then the config file will be `/etc/ssh/ssh_config`
  and if `root` is set then the config file in root's home directory will
  be used.
  (@z38)
- New options:
    - `remote_user` - @z38
    - `user_known_hosts_file` - @gaqzi
    - `strict_host_key_checking` - @gaqzi

## [unversioned initial release] - 2013-11-23

[0.1.0]: https://github.com/gaqzi/ansible-ssh-config/compare/96b7e80e71a4199ff4c5daa4b542adbd46f26a70...v0.1.0
[unversioned initial release]: https://github.com/gaqzi/ansible-ssh-config/commit/96b7e80e71a4199ff4c5daa4b542adbd46f26a70