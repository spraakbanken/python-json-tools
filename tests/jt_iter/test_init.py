import io
import itertools

import pytest

import jt_iter


@pytest.mark.parametrize("data,facit,filetype", [
    (1, "1", "json"),
    (1, "1\n", "jsonl"),
    ([1, 2], "[\n1,\n2\n]", "json"),
    ([1, 2], "1\n2\n", "jsonl"),
])
def test_dump_int_stringio(data, facit, filetype):
    out = io.StringIO()
    jt_iter.dump(data, out, filetype=filetype)
    assert out.getvalue() == facit

    out.seek(0)  # read it from the beginning
    out_iter = jt_iter.load(out, filetype=filetype)
    if isinstance(data, list):
        for i, f in itertools.zip_longest(out_iter, data):
            print("i = {i}".format(i=i))
            assert i is not None
            assert f is not None
            assert i == f
    else:
        for i in jt_iter.load(out, filetype=filetype):
            print("i = {i}".format(i=i))
            assert i == data
