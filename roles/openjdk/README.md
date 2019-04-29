# openjdk

This role installs openjdk.

## Requirements

Before attempting to run any Ansible content you'll need to make sure you've set up the Ansible prequisites per [this document](https://xyleminc.atlassian.net/wiki/spaces/GDO/pages/252904022/How+To+Ansible+Prerequisites)


## Role Variables

#### defaults/main.yml

```
openjdk_version: '1.8.0'

openjdk_cacerts: false
openjdk_s3_bucket: 'sa-releases'
openjdk_s3_cacerts_object: '/certs/cacerts'
openjdk_cacerts_location: '/etc/pki/ca-trust/extracted/java/cacerts'
```

If you want the openjdk role to copy cacerts seed files you must set:

- `openjdk_cacerts: true`
- `openjdk_s3_bucket` to the AWS S3 bucket name that contains your cacerts seed files
- `openjdk_s3_cacerts_object` to the path in your AWS S3 bucket where your seed files exist

## Dependencies

None

## Example Playbook

Typically this role will only be pulled in as a dependency in other roles (i.e. jenkins). However, here is an example playbook if you you'd like to install openjdk independently:


```
- hosts: all
  remote_user: centos
  become: true
  become_user: root

  tasks:
    - name: include openjdk role
      include_role:
        name: openjdk
```

You'll most likely not want to run this on **every** host, so passing the `--limit` argument is especially appropriate when running this playbook:

`ansible-playbook -i inventory inventory/xylem-xcloud/dev openjdk.yml --limit foo.example.com` - where foo.example.com is the name of the host you want to target.


## Author Information
- Michael Johnson - michael.johnson@xyleminc.com
