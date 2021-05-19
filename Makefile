.PHONY: venv help test test-w-coverage bumpversion-minor bumpversion-major bumpversion-patch check-pylint check-mypy check-pylint-refactorings

.default: help

help:
	@echo "usage:"
PLATFORM := ${shell uname -o}
INVENV_PATH = ${shell which invenv}

${info Platform: ${PLATFORM}}
${info invenv: ${INVENV_PATH}}

ifeq (${VIRTUAL_ENV},)
  VENV_NAME = .venv
else
  VENV_NAME = ${VIRTUAL_ENV}
  ${info Using ${VENV_NAME}}
endif
${info Using ${VENV_NAME}}
VENV_BIN = ${VENV_NAME}/bin

ifeq (${INVENV_PATH},)
  INVENV = export VIRTUAL_ENV="${VENV_NAME}"; export PATH="${VENV_BIN}:${PATH}"; unset PYTHON_HOME;
else
  INVENV = invenv -C ${VENV_NAME}
endif

ifeq (${PLATFORM}, Android)
  FLAKE8_FLAGS = --jobs=1
else
  FLAKE8_FLAGS = --jobs=auto
endif


venv: ${VENV_NAME}/venv.created

${VENV_NAME}/venv.created:
	test -d ${VENV_NAME} || python -m venv ${VENV_NAME}
	${INVENV} pip install -U pip wheel
	@touch $@

${VENV_NAME}/dev.installed: setup.py setup.cfg requirements.txt
	${INVENV} pip install -Ue .[dev]
	@touch $@

install-dev: venv ${VENV_NAME}/dev.installed

test: install-dev
	${INVENV} pytest

test-w-coverage: install-dev
	${INVENV} pytest --cov=sb_json_tools --cov-report=term-missing --cov-config=setup.cfg

lint: install-dev
	${INVENV} pylint --rcfile=.pylintrc sb_json_tools

lint-no-fail: install-dev
	${INVENV} pylint --rcfile=.pylintrc --exit-zero sb_json_tools

check-pylint: install-dev
	${INVENV} pylint --rcfile=.pylintrc sb_json_tools

check-mypy: install-dev
	${INVENV} mypy sb_json_tools

check-pylint-refactorings: install-dev
	${INVENV} pylint --disable=C,W,E --enable=R sb_json_tools

bumpversion: install-dev
	${INVENV} bump2version patch

bumpversion-minor: install-dev
	${INVENV} bump2version minor

bumpversion-major: install-dev
	${INVENV} bump2version major

release: bumpversion
release-minor: bumpversion-minor
release-major: bumpversion-major
