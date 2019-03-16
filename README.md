# python-json-tools

Tools for working with json (especially) json-arrays.

Uses `ujson` if present, otherwise standard `json`.

## json-iter (`lib: json_tools.iter`)

Allows you to use `json.load` and `json.dump` with
both json and json-lines files as well as dumping generators.

Regular functions and async functions.

## json-val (`lib: json_tools.val`)

Allows you to validate iterables of json-objects
according to [json-schema](https://wwww.json-schema.org)

Regular and async functions.

## json-diff (`lib: json_tools.diff`)

Allows you to compare two json-objects and get a report
how they differ, if they do.

## json-validator

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

# Installation

If you don't use `pipsi`, you're missing out.
Here are [installation instructions](https://github.com/mitsuhiko/pipsi#readme).

Simply run:

    $ pipsi install .


# Usage

To use it:

    $ json-validator --help
