# control-machine

This role configures an Ansible control machine.

## Requirements

Before attempting to run any Ansible content you'll need to make sure you've set up the Ansible prequisites per [this document](https://xyleminc.atlassian.net/wiki/spaces/GDO/pages/252904022/How+To+Ansible+Prerequisites)

### AWS Tags
| Name          | Values       | Notes  |
| ------------- |------------- | -----  |
| component     | Typically something like **jenkins** or **ansible-control-machine** | This tag is how we'll decide what hosts to target in our playbook |

## Role Variables

#### vars/main.yml

```
control_machine_artifactory_username: 'devops-packages'
control_machine_artifactory_password: '{{ control_machine_vaulted_artifactory_password }}'

control_machine_bitbucket_repo: 'git@bitbucket.org:sensusanalytics-dev/xylem-ansible.git'

control_machine_yum_dependencies:
  - ansible-2.7.7
  - epel-release
  - python2-pip
  - git

control_machine_pip_dependencies:
  - awscli
  - boto

control_machine_ssh_dir: '~/.ssh'
control_machine_ansible_dir: '/etc/ansible'
control_machine_vault_dir: '{{ control_machine_ansible_dir }}/.vault'
control_machine_aws_pem_dir: '{{ control_machine_ansible_dir }}/.aws'
control_machine_aws_config_dir: '~/.aws'
control_machine_git_dir: '~/git'
```

#### vars/vault.yml

```
control_machine_vaulted_artifactory_password: '<artifactory_password>'
```

## Dependencies

None

## Example Playbook

```
- hosts: tag_type_ansible_control_machine
  remote_user: centos
  become: true
  become_user: root
  vars_files:
    - roles/control-machine/vars/vault.yml

  tasks:
    - name: include control-machine role
      include_role:
        name: control-machine
```

## Additional information

For additional information about using this role please refer to [this document](https://xyleminc.atlassian.net/wiki/spaces/GDO/pages/223450359/How+To+Configure+an+Ansible+Control+Machine)

## Author Information
- Michael Johnson - michael.johnson@xyleminc.com
