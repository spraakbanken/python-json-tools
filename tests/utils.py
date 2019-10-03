import itertools


def assert_equal_not_none(i1, i2):
    assert i1 is not None
    assert i2 is not None
    assert i1 == i2


def compare_iters(it1, it2):
    for i1, i2 in itertools.zip_longest(it1, it2):
        assert_equal_not_none(i1, i2)
