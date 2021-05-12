import os

import pytest

from typer.testing import CliRunner

from sb_json_tools import cli


def _to_path(file_name):
    return os.path.join(os.path.dirname(__file__), file_name)


def _invoke_commad(schema, arg):
    return "--schema {0} {1}".format(_to_path(schema), _to_path(arg))


@pytest.fixture
def runner():
    return CliRunner(mix_stderr=False)


def test_cli(runner):
    result = runner.invoke(cli.cli)
    assert result.exit_code == 0
    assert not result.exception
    # assert result.output.strip() == 'Hello, world.'


def test_cli_with_short_option_no_parameter(runner):
    result = runner.invoke(cli.cli, ["-s"])
    assert result.exception
    assert result.exit_code == 2
    # assert result.output.strip() == 'Howdy, world.'


def test_cli_with_long_option_no_parameter(runner):
    result = runner.invoke(cli.cli, ["--schema"])
    assert result.exception
    assert result.exit_code == 2
    # assert result.output.strip() == 'Howdy, world.'


def test_cli_with_short_option_parameter(runner):
    result = runner.invoke(cli.cli, ["-s schema.json"])
    assert result.exception
    assert result.exit_code == 2
    # assert result.output.strip() == 'Howdy, world.'


def test_cli_with_long_option_parameter(runner):
    result = runner.invoke(cli.cli, ["--schema schema.json"])
    assert result.exception
    assert result.exit_code == 2
    # assert result.output.strip() == 'Howdy, world.'


# @pytest.mark.xfail(reason="working on it")
def test_cli_with_schema_and_valid_arg(runner):
    schema = "sb_json_tools/tests/data/schema_default.json"
    arg = "sb_json_tools/tests/data/valid_array.json"
    # with open(schema, "rb") as schema, open(arg, "rb") as arg:
    outfile = "sb_json_tools/tests/data/gen_validated.json"
    result = runner.invoke(cli.cli, ["validate", "--schema", schema, arg, outfile])
    print("result = {result}".format(result=repr(result)))
    assert result.exit_code == 0
    assert not result.exception
    # assert (
    #     result.output.strip()
    #     == "Validating tests/{0} with the schema in tests/{1}.".format(arg, schema)
    # )


@pytest.mark.xfail(reason="working on it")
def test_cli_with_schema_and_invalid_type_arg(runner):
    schema = "sb_json_tools/tests/data/schema_default.json"
    arg = "sb_json_tools/tests/data/invalid_type.json"
    outfile = "sb_json_tools/tests/data/gen_validated.json"
    result = runner.invoke(cli.cli, ["validate", "--schema", schema, arg, outfile])
    print(f"result = {result!r}")
    print(f"result.stdout = {result.stdout}")
    print(f"result.stderr = {result.stderr}")
    assert result.exit_code == 130
    assert not result.exception
    assert result.stdout.strip() == "Validating {0} with the schema in {1}.".format(
        arg, schema
    )


@pytest.mark.xfail(reason="working on it")
def test_cli_with_schema_and_invalid_property_arg(runner):
    schema = "sb_json_tools/tests/data/schema_default.json"
    arg = "sb_json_tools/tests/data/invalid_property.json"
    outfile = "sb_json_tools/tests/data/gen_validated.json"
    result = runner.invoke(cli.cli, ["validate", "--schema", schema, arg, outfile])
    print(f"result = {result!r}")
    print(f"result.stdout = {result.stdout}")
    print(f"result.stderr = {result.stderr}")
    assert result.exit_code == 130
    assert not result.exception
    # assert result.output.strip() == "Validating {0} with the schema in {1}.".format(
    #     arg, schema
    # )
