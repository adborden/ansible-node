.PHONY: lint setup test

PLAYBOOKS := \
  provision.yml \
  reboot.yml \
  upgrade.yml

known_hosts:
	ssh-keyscan $(shell pipenv run ansible-inventory  --list | jq -r '.[] | select(.hosts) | .hosts | flatten | .[]') > $@

lint:
	pipenv run ansible-lint $(PLAYBOOKS)

setup:
	pipenv install --dev

test:
	cd roles/adborden.node && pipenv run molecule test --all
	@echo ok
