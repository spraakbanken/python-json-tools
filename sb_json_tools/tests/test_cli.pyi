from typing import Any

def runner(): ...
def test_cli(runner: Any) -> None: ...
def test_cli_with_short_option_no_parameter(runner: Any) -> None: ...
def test_cli_with_long_option_no_parameter(runner: Any) -> None: ...
def test_cli_with_short_option_parameter(runner: Any) -> None: ...
def test_cli_with_long_option_parameter(runner: Any) -> None: ...
def test_cli_with_schema_and_valid_arg(runner: Any) -> None: ...
def test_cli_with_schema_and_invalid_type_arg(runner: Any) -> None: ...
def test_cli_with_schema_and_invalid_property_arg(runner: Any) -> None: ...
