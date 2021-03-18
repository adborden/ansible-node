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

    assert remotes.contains('smtp port=587')
