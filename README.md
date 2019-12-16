# python-json-tools



[![Build Status](https://travis-ci.org/spraakbanken/python-json-tools.svg?branch=master)](https://travis-ci.org/spraakbanken/python-json-tools)
[![codecov](https://codecov.io/gh/spraakbanken/python-json-tools/branch/master/graph/badge.svg)](https://codecov.io/gh/spraakbanken/python-json-tools)
[![Build Status](https://github.com/spraakbanken/python-json-tools/workflows/Build/badge.svg)](https://github.com/spraakbanken/python-json-tools/actions)
[![PyPI status](https://badge.fury.io/py/sb-json-tools.svg)](https://pypi.org/project/sb-json-tools/)

Tools for working with json (especially) json-arrays.

Uses `ujson` if present, otherwise standard `json`.

## Usage

### Installation
```
pip install sb-json-tools
```
### json-iter (`lib: sb_json_tools.jt_iter`)

Allows you to use `json.load` and `json.dump` with
both json and json-lines files as well as dumping generators.

```
from sb_json_tools import jt_iter

# This command tries to guess format and opens the file
data = jt_iter.load_from_file("data.json") # or data.jsonl

# Write to file, again guessing format
jt_iter.dump_to_file(data, "data.jsonl")
```

```
from sb_json_tools import json_iter, jsonl_iter

# Open and read the file
data = json_iter.load_from_file("data.json")

# Process file

# Write to file
jsonl_iter.dump_to_file(data, "data.jsonl")
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
```
$ make test
```
to setup a virtual environment,
install dev dependencies
and run the unit tests.

*Note:* If you run the command in a activated virtual environment,
that environment is used instead.

