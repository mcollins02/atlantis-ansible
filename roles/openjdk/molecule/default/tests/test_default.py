import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_openjdk_is_installed(host):
    openjdk = host.package("java-1.8.0-openjdk-devel")
    assert openjdk.is_installed
