.PHONY: lint setup test

PLAYBOOKS := \
  provision.yml \
  reboot.yml \
  upgrade.yml

known_hosts:
	ssh-keyscan $(shell poetry run ansible-inventory  --list | jq -r '.[] | select(.hosts) | .hosts | flatten | .[]') > $@

lint:
	poetry run ansible-lint $(PLAYBOOKS)

setup:
	poetry install --with=dev

test:
	cd roles/adborden.node && poetry run molecule test --all
	@echo ok
