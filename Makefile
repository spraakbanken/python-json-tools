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


venv: ${VENV_NAME}/venv.created

${VENV_NAME}/venv.created:
	test -d ${VENV_NAME} || python -m venv ${VENV_NAME}
	@touch $@

${VENV_NAME}/dev.installed: setup.py setup.cfg tools/pip-requires
	${VENV_ACTIVATE}; python -m pip install -e .[dev]
	@touch $@

install-dev: venv ${VENV_NAME}/dev.installed

test: install-dev
	${VENV_ACTIVATE}; pytest --cov=json_tools --cov=jt_diff --cov=jt_iter --cov=jt_val  --cov-report=term-missing tests

VERSION = $(bumpversion --dry-run --list patch | grep old_version | sed -r s."^.*=",,)

bumpversion-patch:
	# bumpversion patch
	$(info verion=${VERSION})

bumpversion-minor:
	bumpversion minor

bumpversion-major:
	bumpversion major
