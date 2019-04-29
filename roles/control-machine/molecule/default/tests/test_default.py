import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_ansible_is_installed(host):
    ansible = host.package("ansible-2.7.7")
    assert ansible.is_installed


def test_epel_is_installed(host):
    epel = host.package("epel-release")
    assert epel.is_installed


def test_python2_pip_is_installed(host):
    python2_pip = host.package("python2-pip")
    assert python2_pip.is_installed


def test_git_is_installed(host):
    git = host.package("git")
    assert git.is_installed


def test_awscli_is_installed(host):
    pip_list = host.pip_package.get_packages(pip_path="/usr/bin/pip")
    assert 'awscli' in pip_list
    assert 'boto' in pip_list


def test_sc_file_exists(host):
    sc_file = host.file("/etc/ansible/.vault/sc")
    with host.sudo():
        assert sc_file.exists


def test_sc_file_mode(host):
    sc_file = host.file("/etc/ansible/.vault/sc").mode
    with host.sudo():
        assert oct(sc_file) == '0600'


def test_ansible_cfg_exists(host):
    ansible_cfg = host.file("/etc/ansible/ansible.cfg")
    with host.sudo():
        assert ansible_cfg.exists


def test_id_rsa_pub_exists(host):
    id_rsa_pub = host.file('/root/.ssh/id_rsa.pub')
    with host.sudo():
        assert id_rsa_pub.exists


def test_id_rsa_exists(host):
    id_rsa = host.file('/root/.ssh/id_rsa')
    with host.sudo():
        assert id_rsa.exists


def test_id_rsa_mode(host):
    id_rsa = host.file('/root/.ssh/id_rsa')
    with host.sudo():
        assert oct((id_rsa).mode) == '0600'


def test_aws_config_exists(host):
    aws_config = host.file('/root/.aws/config')
    with host.sudo():
        assert aws_config.exists


def test_aws_creds_exists(host):
    aws_creds = host.file('/root/.aws/credentials')
    with host.sudo():
        assert aws_creds.exists


def test_git_repo_exists(host):
    git_repo = host.file("/root/git/xylem-ansible")
    with host.sudo():
        assert git_repo.exists
