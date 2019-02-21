setup-dev-env:
	pip install -e .[dev]

test:
	pytest -vv --cov=src tests