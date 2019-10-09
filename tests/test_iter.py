import io
import json

import pytest

from sb_json_tools import json_iter, jsonl_iter
from .utils import compare_iters


DATA = [
    {'a': 1},
    {'a': 2},
]

JSON_FACIT = '[\n{"a": 1},\n{"a": 2}\n]'
JSONL_FACIT = '{"a": 1}\n{"a": 2}\n'


def gen_data():
    for i in DATA:
        yield i

@pytest.mark.parametrize("out", [io.StringIO, io.BytesIO])
@pytest.mark.parametrize(
    "it,data,facit",
    [
        (json_iter, DATA[0], '{"a": 1}'),
        (jsonl_iter, DATA[0], '{"a": 1}\n'),
    ]
)
def test_dump_dict_memoryio(out, it, data, facit):
    out = out()
    if isinstance(out, io.BytesIO):
        facit = facit.encode('utf-8')
    it.dump(data, out)
    assert out.getvalue() == facit

    out.seek(0)
    for i in it.load(out):
        print("i = {i}".format(i=i))
        assert i == data


@pytest.mark.parametrize("out", [io.StringIO, io.BytesIO])
@pytest.mark.parametrize(
    "it,facit",
    [
        (json_iter, JSON_FACIT),
        (jsonl_iter, JSONL_FACIT),
    ]
)
def test_dump_array_memoryio(out, it, facit):
    out = out()
    if isinstance(out, io.BytesIO):
        facit = facit.encode('utf-8')
    it.dump(DATA, out)
    assert facit == out.getvalue()

    out.seek(0)
    compare_iters(it.load(out), DATA)


@pytest.mark.parametrize("out", [io.StringIO, io.BytesIO])
@pytest.mark.parametrize(
    "it,facit",
    [
        (json_iter, JSON_FACIT),
        (jsonl_iter, JSONL_FACIT),
    ]
)
def test_dump_gen_memoryio(out, it, facit):
    out = out()
    if isinstance(out, io.BytesIO):
        facit = facit.encode('utf-8')
    it.dump(gen_data(), out)
    assert facit == out.getvalue()


@pytest.mark.parametrize("file_mode", ["rb", "r"])
@pytest.mark.parametrize(
    "it,file_name,facit",
    [
        (json_iter, "tests/data/array.json", None),
    ]
)
def test_load_file_name(it, file_name: str, facit, file_mode):
    if not facit:
        facit = file_name
    with open(facit) as fp:
        facit_it = json.load(fp)
    test_it = it.load_from_file(file_name, file_mode=file_mode)
    compare_iters(test_it, facit_it)

