import os
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')
files = [
    '/etc/logrotate.d/nginx-paths',
    '/etc/logrotate.d/nginx-options',
    '/etc/logrotate.d/nginx-scripts',
    '/etc/logrotate.d/nginx-rules',
]


@pytest.mark.parametrize('file', files)
def test_configuration_file_exists(host, file):
    file = host.file(file)
    assert file.exists


@pytest.mark.parametrize('file', files)
def test_configuration(host, file):
    cmd = 'logrotate -d ' + file
    result = host.run(cmd)
    assert result.rc == 0
