import io

import pytest

import jt_iter


@pytest.mark.parametrize("data,facit,filetype", [
    (1, "1", "json"),
    (1, "1\n", "jsonl")
])
def test_dump_int_stringio(data, facit, filetype):
    out = io.StringIO()
    jt_iter.dump(data, out, filetype=filetype)
    assert out.getvalue() == facit
