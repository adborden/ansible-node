# ansible-node

Configure a node.

## Usage

Install dependencies.

    make setup

Run the provision playbook.

    poetry run ansible-playbook --extra-vars @vars.yml provision.yml

When inventory hosts change, or when new SSH host keys are generated, update the
known_hosts file.

    rm known_hosts && make known_hosts

## TODO

- [x] node_exporter for prometheus
- [x] email for alerting
- [ ] auto updates
- [x] monit alerting
- [ ] ufw
- [ ] ssh hardening
