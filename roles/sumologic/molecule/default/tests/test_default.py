import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_package(host):
    package = host.package('SumoCollector')
    assert package.is_installed


def test_service(host):
    service = host.service('collector')
    assert service.is_enabled


def test_property_file(host):
    property_file = host.file('/opt/SumoCollector/config/user.properties')
    with host.sudo():
        assert property_file.is_file
        assert property_file.contains('syncSources=/opt/SumoCollector/sources/')
