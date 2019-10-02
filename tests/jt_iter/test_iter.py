import io
import itertools

import pytest

from sb_json_tools.jt_iter import json_iter, jsonl_iter


DATA = [
    {'a': 1},
    {'a': 2},
]

JSON_FACIT = '[\n{"a": 1},\n{"a": 2}\n]'
JSONL_FACIT = '{"a": 1}\n{"a": 2}\n'


def gen_data():
    for i in DATA:
        yield i


@pytest.mark.parametrize(
    "it,data,facit",
    [
        (json_iter, DATA[0], '{"a": 1}'),
        (jsonl_iter, DATA[0], '{"a": 1}\n'),
    ]
)
def test_dump_dict_stringio(it, data, facit):
    out = io.StringIO()
    it.dump(data, out)
    assert out.getvalue() == facit

    out.seek(0)
    for i in it.load(out):
        print("i = {i}".format(i=i))
        assert i == data


@pytest.mark.parametrize(
    "it,facit",
    [
        (json_iter, JSON_FACIT),
        (jsonl_iter, JSONL_FACIT),
    ]
)
def test_dump_array_stringio(it, facit):
    out = io.StringIO()
    it.dump(DATA, out)
    assert facit == out.getvalue()

    out.seek(0)
    for i, f in itertools.zip_longest(it.load(out), DATA):
        assert i is not None
        assert f is not None
        print("i = {i}".format(i=i))
        assert i == f


@pytest.mark.parametrize(
    "it,facit",
    [
        (json_iter, JSON_FACIT),
        (jsonl_iter, JSONL_FACIT),
    ]
)
def test_dump_gen_stringio(it, facit):
    out = io.StringIO()
    it.dump(gen_data(), out)
    assert facit == out.getvalue()

