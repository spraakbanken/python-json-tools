import io

from json_tools.iterate import json_iter as jiter


data = [
    {'a':1},
    {'a':2},
]

facit = '[\n{"a": 1},\n{"a": 2}\n]'


def gen_data():
    for i in data:
        yield i


def test_dump_array_stringio():
    out = io.StringIO()
    jiter.dump_array_json(out, data)
    assert facit == out.getvalue()


def test_dump_gen_stringio():
    out = io.StringIO()
    jiter.dump_array_json(out, gen_data())
    assert facit == out.getvalue()
