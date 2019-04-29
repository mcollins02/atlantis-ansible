import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

def test_terraform_binary(host):
    property_file = host.file('/usr/bin/terraform')
    with host.sudo():
        assert property_file.is_file

def test_atlantis_binary(host):
    property_file = host.file('/usr/bin/atlantis')
    with host.sudo():
        assert property_file.is_file

def test_terragrunt_binary(host):
    property_file = host.file('/usr/bin/terragrunt')
    with host.sudo():
        assert property_file.is_file

def test_service(host):
    service = host.service('atlantis')
    assert service.is_enabled
