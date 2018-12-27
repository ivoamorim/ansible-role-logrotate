import os
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('file, content', [
    ('/etc/logrotate.d/nginx-paths', '/var/log/nginx/path1.log'),
    ('/etc/logrotate.d/nginx-options', '/var/log/nginx/options.log'),
    ('/etc/logrotate.d/nginx-scripts', '/var/log/nginx/scripts.log'),
    ('/etc/logrotate.d/nginx-rules', '/var/log/nginx/rule1.log'),
])
def test_files(host, file, content):
    file = host.file(file)
    assert file.exists
    assert file.contains(content)


@pytest.mark.parametrize('file', [
    ('/etc/logrotate.d/nginx-paths'),
    ('/etc/logrotate.d/nginx-options'),
    ('/etc/logrotate.d/nginx-scripts'),
    ('/etc/logrotate.d/nginx-rules'),
])
def test_configuration(host, file):
    cmd = 'logrotate -d ' + file
    result = host.run(cmd)
    assert result.rc == 0
