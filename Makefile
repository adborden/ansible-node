.PHONY: lint provision setup test


lint:
	pipenv run ansible-lint provision.yml

setup:
	pipenv install --dev

provision:
	pipenv run ansible-playbook --extra-vars @secrets/vars.yml provision.yml

test:
	cd roles/adborden.node && pipenv run molecule test --all
