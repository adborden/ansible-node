.PHONY: lint provision setup test


known_hosts:
	ssh-keyscan $(shell pipenv run ansible-inventory  --list | jq -r '.[] | select(.hosts) | .hosts | flatten | .[]') > known_hosts

lint:
	pipenv run ansible-lint provision.yml

setup:
	pipenv install --dev

provision:
	pipenv run ansible-playbook provision.yml

test:
	cd roles/adborden.node && pipenv run molecule test --all
	@echo ok
