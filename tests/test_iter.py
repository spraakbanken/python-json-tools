import io
import itertools
import json

import pytest

from sb_json_tools import json_iter, jsonl_iter


DATA = [
    {'a': 1},
    {'a': 2},
]

JSON_FACIT = '[\n{"a": 1},\n{"a": 2}\n]'
JSONL_FACIT = '{"a": 1}\n{"a": 2}\n'


def gen_data():
    for i in DATA:
        yield i


def compare_iters(it1, it2):
    for i1, i2 in itertools.zip_longest(it1, it2):
        assert i1 is not None
        assert i2 is not None
        assert i1 == i2


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
    compare_iters(it.load(out), DATA)


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


@pytest.mark.parametrize(
    "it,filename,facit",
    [
        (json_iter, "tests/data/array.json", None),
    ]
)
def test_load_filename(it, filename: str, facit):
    if not facit:
        facit = filename
    with open(facit) as fp:
        facit_it = json.load(fp)
    test_it = it.load_from_file(filename)
    compare_iters(test_it, facit_it)

