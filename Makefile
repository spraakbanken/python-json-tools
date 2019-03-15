.PHONY: venv help test

.default: help

help:
	@echo "usage:"


ifeq (${VIRTUAL_ENV},)
  VENV_NAME = .venv
  VENV_BIN = ${VENV_NAME}/bin
  ${info Using ${VENV_NAME}}
else
  VENV_NAME = ${VIRTUAL_ENV}
  VENV_BIN = ${VENV_NAME}/bin
  ${info Using ${VENV_NAME}}
endif
ifeq (${VIRTUAL_ENV},)
  VENV_ACTIVATE = . ${VENV_BIN}/activate
else
  VENV_ACTIVATE = true
endif
PYTHON = ${VENV_BIN}/python


venv: venv-created

venv-created: ${VENV_NAME}/venv.created
${VENV_NAME}/venv.created:
	test -d ${VENV_NAME} || python -m venv ${VENV_NAME}
	touch $@

${VENV_NAME}/dev.installed: setup.py setup.cfg tools/pip-requires
	${PYTHON} -m pip install .[dev]
	touch $@

install-dev: venv ${VENV_NAME}/dev.installed

test: install-dev
	${PYTHON} -m pytest tests
