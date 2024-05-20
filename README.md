# sb-json-tools

[![PyPI version](https://badge.fury.io/py/sb-json-tools.svg)](https://pypi.org/project/sb-json-tools/)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/sb-json-tools)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/sb-json-tools)](https://pypi.org/project/sb-json-tools/)

[![Maturity badge - level 3](https://img.shields.io/badge/Maturity-Level%203%20--%20Stable-green.svg)](https://github.com/spraakbanken/getting-started/blob/main/scorecard.md)
[![Stage](https://img.shields.io/pypi/status/sb-json-tools)](https://pypi.org/project/sb-json-tools/)

[![Code Coverage](https://codecov.io/gh/spraakbanken/python-json-tools/branch/main/graph/badge.svg)](https://codecov.io/gh/spraakbanken/python-json-tools/)

[![CI(check)](https://github.com/spraakbanken/python-json-tools/actions/workflows/check.yml/badge.svg)](https://github.com/spraakbanken/python-json-tools/actions/workflows/check.yml)
[![CI(release)](https://github.com/spraakbanken/python-json-tools/actions/workflows/release.yml/badge.svg)](https://github.com/spraakbanken/python-json-tools/actions/workflows/release.yml)
[![CI(scheduled)](https://github.com/spraakbanken/python-json-tools/actions/workflows/scheduled.yml/badge.svg)](https://github.com/spraakbanken/python-json-tools/actions/workflows/scheduled.yml)
[![CI(test)](https://github.com/spraakbanken/python-json-tools/actions/workflows/test.yml/badge.svg)](https://github.com/spraakbanken/python-json-tools/actions/workflows/test.yml)

Tools for working with json (especially) json-arrays.

Uses `orjson` if present, otherwise standard `json`.

## Usage

### Installation

```bash
pip install sb-json-tools
```

## json-val (`lib: sb_json_tools.jt_val`)

Allows you to validate iterables of json-objects
according to [json-schema](https://wwww.json-schema.org)

Regular and async functions.

## json-diff (`lib: sb_json_tools.jsondiff`)

Allows you to compare two json-objects and get a report
how they differ, if they do.

## json-val

Command-line tool to validate a json-file with a schema [json-schema](http://json-schema.org).

# Development

After cloning the repo, just run

```bash
make dev
make test
```

to setup a virtual environment,
install dev dependencies
and run the unit tests.

_Note:_ If you run the command in a activated virtual environment,
that environment is used instead.
