"""Role testing files using testinfra."""


def test_hosts_file(host):
    """Validate /etc/hosts file."""
    f = host.file("/etc/hosts")

    assert f.exists
    assert f.user == "root"
    assert f.group == "root"


def test_nullmailer_remotes(host):
    """Assert remotes config file exists."""
    remotes = host.file('/etc/nullmailer/remotes')

    assert remotes.exists
    assert remotes.user == 'mail'
    assert remotes.group == 'mail'
    assert remotes.mode == 0o600
    assert remotes.contains('smtp port=587')


def test_nullmailer_adminaddr(host):
    """Assert adminaddr config file exists."""
    conf = host.file('/etc/nullmailer/adminaddr')

    assert conf.exists
    assert conf.user == 'mail'
    assert conf.group == 'mail'
    assert conf.mode == 0o644
    assert conf.contains('admin@example.com')


def test_monit_monitrc(host):
    """Assert monit config file exists."""
    conf = host.file('/etc/monit/monitrc')

    assert conf.exists
    assert conf.user == 'root'
    assert conf.group == 'root'
    assert conf.mode == 0o600
    assert conf.contains('set alert monit@example.com')
    assert conf.contains('allow admin:monit-password')


def test_monit_common_cron(host):
    """Assert monit common config file is enabled."""
    conf = host.file('/etc/monit/conf-enabled/cron')

    assert conf.exists
    assert conf.is_symlink
    assert conf.linked_to == '/etc/monit/conf-available/cron'
    assert conf.user == 'root'
    assert conf.group == 'root'


def test_monit_common_openssh(host):
    """Assert monit common config file is enabled."""
    conf = host.file('/etc/monit/conf-enabled/openssh-server')

    assert conf.exists
    assert conf.is_symlink
    assert conf.linked_to == '/etc/monit/conf-available/openssh-server'
    assert conf.user == 'root'
    assert conf.group == 'root'


def test_monit_root(host):
    """Assert monit root config file exists."""
    conf = host.file('/etc/monit/conf.d/root')

    assert conf.exists
    assert conf.user == 'root'
    assert conf.group == 'root'
    assert conf.mode == 0o644
    assert conf.contains('root')


def test_monit_prometheus_node_exporter(host):
    """Assert monit prometheus-node-exporter config file exists."""
    conf = host.file('/etc/monit/conf.d/prometheus-node-exporter')

    assert conf.exists
    assert conf.user == 'root'
    assert conf.group == 'root'
    assert conf.mode == 0o644
    assert conf.contains('prometheus-node-exporter')
