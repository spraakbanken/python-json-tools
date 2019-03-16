import pytest

from json_tools import diff

objs = [
{
	'a': 1
},
{
    'a': 2
},
{
    'a': 1,
    'b': 1
},
]

indices = [i for i in range(len(objs))]

def change(before, after, field):
    return {
        'before': before,
        'after': after,
        'field': field,
        'type': 'CHANGE'
    }


def added(after, field):
    return {
        'after': after,
        'field': field,
        'type': 'ADDED'
    }


def removed(before, field):
    return {
        'before': before,
        'field': field,
        'type': 'REMOVED'
    }


facit = [
    [
        [] for _ in indices
    ] for _ in indices
]


facit[0][1] = [change(1,2,'a')]
facit[0][2] = [added(1,'b')]
facit[1][0] = [change(2,1,'a')]
facit[1][2] = [change(2,1,'a'),added(1,'b')]
facit[2][0] = [removed(1,'b')]
facit[2][1] = [change(1,2,'a'),removed(1,'b')]


def test_setup():
    assert len(objs) == len(indices)
    assert len(facit) == len(indices)
    for row in facit:
        assert len(row) == len(indices)


@pytest.mark.parametrize('i2', indices)
@pytest.mark.parametrize('i1', indices)
def test_compare(i1, i2):
    r = diff.compare(objs[i1], objs[i2])

    assert len(r) == len(facit[i1][i2])

    for a, b in zip(r, facit[i1][i2]):
        assert a == b