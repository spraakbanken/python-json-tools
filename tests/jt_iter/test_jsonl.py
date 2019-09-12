import io

from jt_iter import jsonl_iter as jiter


data = [
    {'a': 1},
    {'a': 2},
]

facit = '{"a": 1}\n{"a": 2}\n'


def gen_data():
    for i in data:
        yield i


def test_dump_dict_stringio():
    out = io.StringIO()
    jiter.dump(data[0], out)
    assert out.getvalue() == '{"a": 1}\n'

    out.seek(0)
    for i in jiter.load(out):
        print("i = {i}".format(i=i))
        assert i == data[0]


def test_dump_array_stringio():
    out = io.StringIO()
    jiter.dump(data, out)
    assert facit == out.getvalue()


def test_dump_gen_stringio():
    out = io.StringIO()
    jiter.dump(gen_data(), out)
    assert facit == out.getvalue()
