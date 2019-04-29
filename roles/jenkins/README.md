
# jenkins

This role installs jenkins and provides you with the temporary admin password.


## Requirements

Before attempting to run any Ansible content you'll need to make sure you've set up the Ansible prequisites per [this document](https://xyleminc.atlassian.net/wiki/spaces/GDO/pages/252904022/How+To+Ansible+Prerequisites)

### AWS Tags
| Name          | Values       | Notes  |
| ------------- |------------- | -----  |
| component     | Typically something like **jenkins** or **action-guide** | This component is how we'll decide what hosts to target in our playbook |


## Role Variables

#### vars/main.yml

```
jenkins_ec2: true

jenkins_user: 'jenkins'
jenkins_group: 'jenkins'
jenkins_home: '/jenkins'
jenkins_docker_group: 'docker'
jenkins_docker_home: '/var/lib/docker'

jenkins_port: '8080'
jenkins_http_host: '0.0.0.0'
jenkins_http_port: '8080'
jenkins_log_dir: '{{ jenkins_home }}/logs'
jenkins_ebs_vol: '/dev/xvdf'
jenkins_docker_ebs_vol: '/dev/xvdg'
jenkins_max_mem: '512M'

jenkins_ansible_dir: '/etc/ansible'
jenkins_vault_dir: '{{ jenkins_ansible_dir }}/.vault'
jenkins_aws_pem_dir: '{{ jenkins_ansible_dir }}/.aws'
jenkins_aws_config_dir: '~/.aws'

jenkins_artifactory_path: 'https://xylem.jfrog.io/xylem/devops-packages'
jenkins_artifactory_username: 'devops-packages'
jenkins_artifactory_password: '{{ jenkins_vaulted_artifactory_password }}'

jenkins_yum_dependencies:
  - epel-release
  - ansible
  - binutils
  - createrepo
  - docker-ce-18.09.2
  - dkms
  - git
  - gcc
  - glibc-devel
  - glibc-headers
  - jenkins-2.166
  - kernel-devel
  - kernel-headers
  - libgomp
  - libselinux-python
  - make
  - openssl-devel
  - patch
  - python-devel
  - python2-pip
  - rpm-build
  - ruby-devel
  - rubygems
  - rubygem-rake
  - vagrant-2.2.3
  - VirtualBox-6.0

jenkins_pip_dependencies:
  - awscli
  - boto
  - molecule
  - python-vagrant
  - requests==2.21.0

jenkins_ruby_gems:
  - fpm
  - xvfb

jenkins_binary_dependencies:
  - kubectl
  - aws-iam-authenticator
  - helm
  - tiller
  - packer
```
#### vars/vault.yml

```
jenkins_vaulted_artifactory_password: '<artifcatory_password>'
```

## Dependencies

This role depends on the openjdk role.

#### meta/main.yml

```
dependencies:
  - role: openjdk
```


## Example Playbook

```
- hosts: tag_type_jenkins
  remote_user: centos
  become: true
  become_user: root
  vars_files:
    - roles/jenkins/vars/vault.yml

  tasks:
    - name: include jenkins role
      include_role:
        name: jenkins
```

## Additional information

For additional information about using this role please refer to [this document](https://xyleminc.atlassian.net/wiki/spaces/GDO/pages/230490591/How+To+Configure+Jenkins)


## Author Information
- Michael Johnson - michael.johnson@xyleminc.com
