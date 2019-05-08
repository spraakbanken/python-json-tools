import os

import pytest

from click.testing import CliRunner

from json_tools.val import cli


def _to_path(filename):
    return os.path.join(os.path.dirname(__file__), filename)


def _invoke_commad(schema, arg):
    return '--schema {0} {1}'.format(_to_path(schema), _to_path(arg))


@pytest.fixture
def runner():
    return CliRunner()


def test_cli(runner):
    result = runner.invoke(cli.main)
    assert result.exit_code == 2
    assert result.exception
    # assert result.output.strip() == 'Hello, world.'


def test_cli_with_short_option_no_parameter(runner):
    result = runner.invoke(cli.main, ['-s'])
    assert result.exception
    assert result.exit_code == 2
    # assert result.output.strip() == 'Howdy, world.'


def test_cli_with_long_option_no_parameter(runner):
    result = runner.invoke(cli.main, ['--schema'])
    assert result.exception
    assert result.exit_code == 2
    # assert result.output.strip() == 'Howdy, world.'


def test_cli_with_short_option_parameter(runner):
    result = runner.invoke(cli.main, ['-s schema.json'])
    assert result.exception
    assert result.exit_code == 2
    # assert result.output.strip() == 'Howdy, world.'


def test_cli_with_long_option_parameter(runner):
    result = runner.invoke(cli.main, ['--schema schema.json'])
    assert result.exception
    assert result.exit_code == 2
    # assert result.output.strip() == 'Howdy, world.'


def test_cli_with_schema_and_valid_arg(runner):
    schema = "tests/data/schema_default.json"
    arg = "tests/valid_array.json"
    result = runner.invoke(cli.main, [
        '--schema',
        schema,
        arg,
    ])
    assert result.exit_code == 0
    assert not result.exception
    assert (
        result.output.strip()
        ==
        'Validating tests/{0} with the schema in tests/{1}.'.format(arg, schema)
    )


def test_cli_with_schema_and_invalid_type_arg(runner):
    schema = "tests/data/schema_default.json"
    arg = "tests/data/invalid_type.json"
    result = runner.invoke(cli.main, ['--schema', schema, arg])
    assert result.exit_code == 0
    assert not result.exception
    assert result.output.strip() == 'Validating {0} with the schema in {1}.'.format(arg, schema)


def test_cli_with_schema_and_invalid_property_arg(runner):
    schema = "schema.json"
    arg = "invalid_property.json"
    result = runner.invoke(cli.main, ['--schema {0} {1}'.format(schema, arg)])
    assert result.exit_code == 0
    assert not result.exception
    assert result.output.strip() == 'Validating {0} with the schema in {1}.'.format(arg, schema)
