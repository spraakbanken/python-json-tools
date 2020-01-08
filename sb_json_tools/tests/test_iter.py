import io
import json
from string import printable

import pytest
from hypothesis import given, strategies as st

from sb_json_tools import json_iter, jsonl_iter
from sb_json_tools.tests.utils import compare_iters


DATA = [
    {"a": 1},
    {"a": 2},
]

JSON_FACIT = '[\n{"a": 1},\n{"a": 2}\n]'
JSONL_FACIT = '{"a": 1}\n{"a": 2}\n'

json_data = st.recursive(
    st.none()
    | st.booleans()
    | st.integers()
    #| st.floats(allow_nan=False, allow_infinity=False)
    | st.text(printable),
    lambda children: st.lists(children, 1).filter(lambda l: len(l) > 1 or l[0] is None)
    | st.dictionaries(
        st.text(printable).filter(lambda s: len(s) > 0), children, min_size=1
    ),
)


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
@given(json_data)
def test_dump_array_memoryio(out, it, data):
    out = out()
    it.dump(data, out)

    out.seek(0)
    if isinstance(data, list):
        compare_iters(it.load(out), data)
    else:
        for i, obj in enumerate(it.load(out)):
            if i == 0:
                assert obj == data
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

