# trend

This role installs trend, registers it, and sends a slack notifcation for new installs. However, trend is currently baked into our golden AMI so the only need to run this would be to update the agent version.

## Requirements

Before attempting to run any Ansible content you'll need to make sure you've set up the Ansible prequisites per [this document](https://xyleminc.atlassian.net/wiki/spaces/GDO/pages/252904022/How+To+Ansible+Prerequisites)

### AWS Tags

| Name          | Values       | Notes  |
| ------------- |------------- | -----  |
| component     | Typically something like **action-guide** or **priority-devices** or **jenkins** | This tag is how we'll decide what hosts to target in our playbook |
| env           | Typically something like **dev** or **prod** or **canada**| Used when sending notification to the  #trend-installs slack channel |


## Role Variables

#### defaults/main.yml

```
trend_version: '10.0.0-2856'

trend_artifactory_path: 'https://xylem.jfrog.io/xylem/devops-packages'
trend_artifactory_username: 'devops-packages'
trend_artifactory_password: '{{ vaulted_trend_artifactory_password }}'

trend_env: '{{ hostvars[inventory_hostname]["ec2_tag_env"] }}'
trend_hostname: '{{ hostvars[inventory_hostname]["ec2_tag_Name"] }}' 

trend_tenantID: '{{ vaulted_trend_tenantID }}'
trend_token: '{{ vaulted_trend_token }}'
trend_policy_id: 1

trend_slack_notify_enabled: true
trend_slack_token: '{{ vaulted_trend_slack_token }}'
```

#### defaults/vault.yml

```
vaulted_trend_artifactory_password: '<trend_artifactory_password>'
vaulted_trend_tenantID: '<trend_tenantID>'
vaulted_trend_token: '<trend_token>'
vaulted_trend_slack_token: '<trend_slack_token>'
```

## Dependencies

None

## Example Playbook

Install and configure trend on an app server:

```
- hosts: tag_component_action_guide
  remote_user: centos
  become: true
  become_user: root
  vars_files:
    - roles/trend/defaults/vault.yml

  tasks:
    - name: include trend role
      include_role:
        name: trend
```

Install and configure trend on devops infra:

```
- hosts: tag_component_jenkins
  remote_user: centos
  become: true
  become_user: root
  vars_files:
    - roles/trend/defaults/vault.yml

  tasks:
    - name: include trend role
      include_role:
        name: trend
```

## Author Information
- Michael Johnson - michael.johnson@xyleminc.com
