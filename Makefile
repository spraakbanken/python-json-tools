.PHONY: venv help test bumpversion-minor bumpversion-major bumpversion-patch

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
	${VENV_ACTIVATE}; python -m pip install -Ue .[dev]
	@touch $@

install-dev: venv ${VENV_NAME}/dev.installed

test: install-dev
	${VENV_ACTIVATE}; pytest --cov=sb_json_tools  --cov-report=term-missing tests

lint: install-dev
	${VENV_ACTIVATE}; pylint --rcfile=.pylintrc sb_json_tools tests

bumpversion-patch: install-dev
	${VENV_ACTIVATE}; bump2version patch

bumpversion-minor: install-dev
	${VENV_ACTIVATE}; bump2version minor

bumpversion-major: install-dev
	${VENV_ACTIVATE}; bump2version major

release-patch: bumpversion-patch
release-minor: bumpversion-minor
release-major: bumpversion-major
