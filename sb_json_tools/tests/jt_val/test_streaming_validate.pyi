from typing import Any

schema: Any

def gen_valid_data(n: Any) -> None: ...
def gen_invalid_data(n: Any) -> None: ...
def gen_mixed_data(n: Any) -> None: ...
def test_valid_data() -> None: ...
def test_invalid_data() -> None: ...
def test_mixed_data() -> None: ...
