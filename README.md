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

## Development

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

### Make a release

1. Make changes and commit.
2. Update CHANGELOG.md:
   1. If [git-cliff](https://git-cliff.org) is installed, run `make prepare-release` and then manually update the CHANGELOG.md. Commit the changes. (If the commit message start with `chore(release): prepare for`, git-cliff will ignore the commit.)
   2. Without `git-cliff` add the relevant information with format below, above the latest release.

      ```markdown
      ## [unreleased]

      ### Added
      - new features

      ### Fixed
      - fixed a bug
      ```

      Commit the changes. (If the commit message start with `chore(release): prepare for`, git-cliff will ignore the commit.)
3. Bump the version:

   ```bash
   # Install dependencies for bumping the version
   make install-dev-release
   # Bump the version, choose what part by giving part= at command line
   # Bump the patch part [X.Y.Z -> X.Y.(Z+1)]
   make bumpversion
   # bump the minor part [X.Y.Z -> X.(Y+1).0]
   make bumpversion part=minor
   # bump the major part [X.Y.Z -> (X+1).0.0]
   make bumpversion part=major
   ```

   [`bump-my-version`](https://callowayproject.github.io/bump-my-version/) will commit and tag the bumping.
4. Push the tag to GitHub for the [release](.github/workflows/release.yml) workflow to build and publish the release to [PyPi](https://pypi.org).
   1. Either by running `make publish` (or `make publish branch=<BRANCH_NAME>` if not on main)
   2. Or by running `git push origin main --tags`
