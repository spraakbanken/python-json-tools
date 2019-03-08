.PHONY: test

default: test

VENV_ACTIVATE=. ./.venv/bin/activate

.venv/created:
	test -d $(@D) || python -m venv $(@D)
	# $(VENV_ACTIVATE) \
	# && pip install pip-tools
	touch $@

.venv/requirements-test.installed: .venv/created setup.py
	$(VENV_ACTIVATE) && \
	pip install -e .[dev]
	touch $@

setup-dev-env: .venv/requirements-test.installed

test: setup-dev-env
	$(VENV_ACTIVATE) && pytest -vv --cov=src tests
