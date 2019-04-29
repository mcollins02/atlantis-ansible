# sumologic

This role installs and configures sumologic.

## Requirements

Before attempting to run any Ansible content you'll need to make sure you've set up the Ansible prequisites per [this document](https://xyleminc.atlassian.net/wiki/spaces/GDO/pages/252904022/How+To+Ansible+Prerequisites)

### AWS Tags

| Name          | Values       | Notes  |
| ------------- |------------- | -----  |
| component     | Typically something like **action-guide** or **priority-devices** or **jenkins** | This tag is how we'll decide what hosts to target in our playbook |
| env           | Typically something like **dev** or **prod** or **canada**| Used when templating sources.json and user_properties.json |


## Role Variables

#### vars/main.yml

```
sumologic_accessid: '{{ vaulted_sumologic_accessid }}'
sumologic_accesskey: '{{ vaulted_sumologic_accesskey }}'
```

#### vars/vault.yml

```
vaulted_sumologic_accessid: '<sumologic_accessid>'
vaulted_sumologic_accesskey: '<sumologic_accesskey>'
```

#### defaults/main.yml

```
sumologic_version: '19.227-15'
sumlogic_app_logpath: '/opt/sensus/**/*.log'
sumologic_name: '{{ hostvars[inventory_hostname]["ansible_facts"]["fqdn"] }}'

sumologic_collector_config_path: '/opt/SumoCollector/config'

sumologic_collector_sources_path: '/opt/SumoCollector/sources'
autolinematching:
  useAutolineMatching: false
  manualPrefixRegexp: '^\\d{4}-\\d{2}-\\d{2}\\s\\d{2}:\\d{2}:\\d{2},\\d{3}\\s\\|.*'

sumologic_skip_autoline_apps:
  - action-guide
  - priority-devices
  - rni-integration
```
To skip autoline for a particular app, add the app to the `sumologic_skip_autoline_apps` list. The name in the list **must** match the name supplied to the `component` AWS tag.

## Dependencies

None

## Example Playbook

Install and configure sumologic on an app server:

```
- hosts: tag_component_action_guide
  remote_user: centos
  become: true
  become_user: root
  vars_files:
    - roles/sumologic/vars/vault.yml

  tasks:
    - name: include control-machine role
      include_role:
        name: control-machine
```

Install and configure sumologic on devops infra:

```
- hosts: tag_component_jenkins
  remote_user: centos
  become: true
  become_user: root
  vars_files:
    - roles/sumologic/vars/vault.yml

  tasks:
    - name: include control-machine role
      include_role:
        name: control-machine
```

## Author Information
- Michael Johnson - michael.johnson@xyleminc.com
