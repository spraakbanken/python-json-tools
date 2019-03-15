.PHONY: venv help test

.default: help

help:
	@echo "usage:"

VENV_NAME = .venv
VENV_BIN = ${VENV_NAME}/bin
ifeq (${VIRTUAL_ENV},)
	VENV_ACTIVATE = . ${VENV_BIN}/activate
else
	VENV_ACTIVATE = true
PYTHON = ${VENV_BIN}/python

install-dev:
    pipenv install --dev

test:
	pipenv run py.test tests
