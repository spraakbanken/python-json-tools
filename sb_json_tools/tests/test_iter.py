import io
import json
from string import printable

import pytest
import hypothesis
from hypothesis import given, settings, strategies as st

from sb_json_tools import json_iter, jsonl_iter
from sb_json_tools.tests.utils import (
    compare_iters,
    JSON_DATA,
    convert_to_decimal_if_float,
    reference_dict,
)


DATA = [
    {"a": 1},
    {"a": 2},
]

JSON_FACIT = '[\n{"a": 1},\n{"a": 2}\n]'
JSONL_FACIT = '{"a": 1}\n{"a": 2}\n'


def gen_data():
    for i in DATA:
        yield i


@pytest.mark.parametrize("out", [io.StringIO, io.BytesIO])
@pytest.mark.parametrize(
    "it,data", [(json_iter, DATA[0]), (jsonl_iter, DATA[0]),],
)
def test_dump_dict_memoryio(out, it, data):
    out = out()
    it.dump(data, out)

    out.seek(0)
    for i, obj in enumerate(it.load(out)):
        if i == 0:
            assert obj == data
        else:
            pytest.fail()


@pytest.mark.parametrize("out", [io.StringIO, io.BytesIO])
@pytest.mark.parametrize("it", [json_iter, jsonl_iter])
@given(st.just("00"))
def test_dump_strings_with_zeros_memoryio(out, it, data):
    out = out()
    it.dump(data, out)
    facit = '"00"'
    if isinstance(out, io.BytesIO):
        facit = facit.encode("utf-8")
    assert out.getvalue() == facit

    out.seek(0)
    for i, obj in enumerate(it.load(out)):
        if i == 0:
            assert obj == data
        else:
            pytest.fail()

    # out.seek(0)
    # if not isinstance(data, list):
    #     data = [data]
    # compare_iters(it.load(out), data)


@pytest.mark.parametrize("out", [io.StringIO, io.BytesIO])
@pytest.mark.parametrize("it", [json_iter, jsonl_iter])
@given(JSON_DATA)
@hypothesis.settings(suppress_health_check=[hypothesis.HealthCheck.too_slow])
def test_dump_array_memoryio(out, it, data):
    out = out()
    it.dump(data, out)

    facit = reference_dict(data)

    out.seek(0)
    if isinstance(data, list):
        compare_iters(it.load(out), facit)
    else:
        for i, obj in enumerate(it.load(out)):
            if i == 0:
                assert obj == facit
            else:
                pytest.fail()


@pytest.mark.parametrize("out", [io.StringIO, io.BytesIO])
@pytest.mark.parametrize(
    "it, data_generator", [(json_iter, gen_data), (jsonl_iter, gen_data),]
)
def test_dump_gen_memoryio(out, it, data_generator):
    out = out()
    it.dump(data_generator(), out)
    out.seek(0)
    compare_iters(it.load(out), data_generator())


@pytest.mark.parametrize("file_mode", ["rb", "r"])
@pytest.mark.parametrize(
    "it,file_name,facit", [(json_iter, "sb_json_tools/tests/data/array.json", None),]
)
def test_load_file_name(it, file_name: str, facit, file_mode):
    if not facit:
        facit = file_name
    with open(facit) as fp:
        facit_it = json.load(fp)
    test_it = it.load_from_file(file_name, file_mode=file_mode)
    compare_iters(test_it, facit_it)

