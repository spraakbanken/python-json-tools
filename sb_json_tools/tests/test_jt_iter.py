import io

import pytest

import hypothesis
from hypothesis import given, strategies as st

from sb_json_tools import jt_iter, jsonlib

from sb_json_tools.tests.utils import (
    compare_iters,
    JSON_DATA,
    convert_to_decimal_if_float,
    reference_dict,
)


@pytest.mark.parametrize("out", [io.StringIO, io.BytesIO])
@pytest.mark.parametrize(
    "file_type", ["json", "jsonl"],
)
@given(JSON_DATA)
@hypothesis.settings(suppress_health_check=[hypothesis.HealthCheck.too_slow])
def test_dump_and_load_memoryio(out, file_type, data):
    out = out()
    jt_iter.dump(data, out, file_type=file_type)
    facit = reference_dict(data)

    out.seek(0)  # read it from the beginning
    if isinstance(data, list):
        out_iter = jt_iter.load(out, file_type=file_type)
        compare_iters(out_iter, facit)
    else:
        for i in jt_iter.load(out, file_type=file_type):
            assert i == facit
