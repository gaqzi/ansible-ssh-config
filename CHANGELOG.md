# Change Log

## [0.3.0] - 2015-11-03
### Changed

- Moved the module to `library/` to allow for easy install as a role
  in Ansible Galaxy.

- Submitted to Ansible Galaxy which was suggested by @MartinNowak on GitHub

## [0.2.0] - 2015-08-19
### Changed

- Convert all keywords to CamelCase in the SSH config file.

  NOTE: If you get the new version of this plugin it'll change all the current
  keys to conform.
  (@bwaldvogel on GitHub)
- Allow SSH to do home directory expansion for `identity_file`

  When providing a value to `identity_file` such as:

  > ~/.ssh/foo

  the path name should be passed as-is for writing to the template, since ssh
  itself is smart enough to perform home directory expansion.
  (@conorsch on GitHub)
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

[0.3.0]: https://github.com/gaqzi/ansible-ssh-config/compare/v0.2.0...v0.3.0
[0.2.0]: https://github.com/gaqzi/ansible-ssh-config/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/gaqzi/ansible-ssh-config/compare/96b7e80e71a4199ff4c5daa4b542adbd46f26a70...v0.1.0
[unversioned initial release]: https://github.com/gaqzi/ansible-ssh-config/commit/96b7e80e71a4199ff4c5daa4b542adbd46f26a70
