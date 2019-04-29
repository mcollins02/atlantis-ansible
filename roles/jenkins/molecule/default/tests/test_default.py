import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_jenkins_home_mounted(host):
    jenkins = host.mount_point("/jenkins")
    assert jenkins.exists


def test_jenkins_ext4(host):
    jenkins = host.mount_point("/jenkins")
    assert jenkins.filesystem == 'ext4'


def test_jenkins_is_installed(host):
    jenkins = host.package("jenkins")
    assert jenkins.is_installed


def test_jenkins_running_and_enabled(host):
    jenkins = host.service("jenkins")
    assert jenkins.is_running
    assert jenkins.is_enabled


def test_jenkins_is_listening(host):
    jenkins = host.socket("tcp://127.0.0.1:8080")
    assert jenkins.is_listening
