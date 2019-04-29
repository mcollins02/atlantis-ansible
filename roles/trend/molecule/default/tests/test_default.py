import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_trend_is_installed(host):
    trend = host.package("ds_agent")
    assert trend.is_installed


def test_trend_running_and_enabled(host):
    trend = host.service("ds_agent")
    assert trend.is_running
    assert trend.is_enabled


def test_ds_agent_config_file(host):
    ds_agent_config = host.file('/var/opt/ds_agent/dsa_core/ds_agent.config')
    with host.sudo():
        assert ds_agent_config.is_file
