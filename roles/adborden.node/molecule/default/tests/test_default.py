"""Role testing files using testinfra."""

deploy_user = 'deploy'
deploy_home = '/var/lib/deploy'


def test_hosts_file(host):
    """Validate /etc/hosts file."""
    f = host.file("/etc/hosts")

    assert f.exists
    assert f.user == "root"
    assert f.group == "root"


def test_deploy_user(host):
    """Assert deploy user exists."""
    deploy = host.user(deploy_user)

    assert deploy.exists
    assert len(deploy.groups) == 1
    assert deploy_user in deploy.groups
    assert deploy.groups == [deploy_user]
    assert deploy.home == deploy_home
    assert deploy.password == '!'


def test_deploy_home(host):
    """Assert deploy user home dir exists."""
    deploy = host.file(deploy_home)

    assert deploy.exists
    assert deploy.is_directory
    # TODO this should be 0o750
    assert deploy.mode == 0o755
    assert deploy.user == deploy_user
    assert deploy.group == deploy_user


def test_deploy_ssh_dir(host):
    """Assert deploy user ssh dir is configured."""
    deploy = host.file('%s/.ssh' % deploy_home)

    assert deploy.exists
    assert deploy.is_directory
    assert deploy.mode == 0o700
    assert deploy.user == deploy_user
    assert deploy.group == deploy_user


def test_deploy_ssh_authorized_keys(host):
    """Assert deploy user is configured with authorized_keys."""
    deploy = host.file('%s/.ssh/authorized_keys' % deploy_home)

    assert deploy.exists
    assert deploy.mode == 0o600
    assert deploy.user == deploy_user
    assert deploy.group == deploy_user
    assert deploy.content == b'ssh-rsa key-data-test comment\n'


def test_deploy_sudo(host):
    """Assert deploy user is configured with sudo access."""
    deploy = host.file('/etc/sudoers.d/90-deploy.conf')

    assert deploy.exists
    assert deploy.mode == 0o440
    assert deploy.user == 'root'
    assert deploy.group == 'root'
    assert deploy.content == b'deploy ALL=(ALL) NOPASSWD:ALL\n'


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
