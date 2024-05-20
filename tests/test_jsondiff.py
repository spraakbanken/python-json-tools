from string import printable

import pytest

from hypothesis import given, strategies as st

from sb_json_tools import jsondiff as diff




objs = [
    {'a': 1},  # 0
    {'a': 2},  # 1
    {'a': 1, 'b': 1},  # 2
    {'a': '1'},  # 3
    {'a': {'s': [1]}},  # 4
    {'a': {'s': [1, 2]}},  # 5
    {'a': {'s': '1'}},  # 6
]

indices = [i for i in range(len(objs))]


def change(field, before, after):
    return {'before': before, 'after': after, 'field': field, 'type': 'CHANGE'}


def typechange(field, before, after):
    return {
        'before': before,
        'after': after,
        'field': field,
        'type': 'TYPECHANGE'
        }


def added(field, after):
    return {'after': after, 'field': field, 'type': 'ADDED'}


def removed(field, before):
    return {'before': before, 'field': field, 'type': 'REMOVED'}


_data_test_compare = [
    (0, 1, [change('a', 1, 2)]),
    (0, 2, [added('b', 1)]),
    (0, 3, [typechange('a', 'int', 'str'), change('a', 1, '1')]),
    (0, 4, [typechange('a', 'int', 'dict'), change('a', 1, {'s': [1]})]),
    (1, 0, [change('a', 2, 1)]),
    (1, 2, [change('a', 2, 1), added('b', 1)]),
    (2, 0, [removed('b', 1)]),
    (2, 1, [change('a', 1, 2), removed('b', 1)]),
    (4, 5, [added('a.s[1]', 2)]),
    (4, 6, [
        typechange('a.s', 'list', 'str'),
        change('a.s', [1], '1'),
        typechange('a.s[0]', 'int', 'str'),
        change('a.s[0]', 1, '1'),
    ]),
]
for i in range(len(objs)):
    _data_test_compare.append((i, i, []))


@pytest.mark.parametrize('i1,i2,facit', _data_test_compare)
def test_compare(i1, i2, facit):
    r = diff.compare(objs[i1], objs[i2])

    assert len(r) == len(facit)

    for a in r:
        assert a in facit


@given(st.dictionaries(st.text(printable), st.none() | st.floats(allow_nan=False) | st.integers() | st.text(printable)))
def test_diff_equal(data):
    r = diff.compare(data, data)

    assert len(r) == 0

