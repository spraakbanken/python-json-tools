import itertools
import decimal


def assert_equal_not_none(i1, i2):
    assert i1 is not None
    assert i2 is not None
    if isinstance(i1, decimal.Decimal) and isinstance(i2, float):
        assert i1 == decimal.Decimal(i2)
    else:
        assert i1 == i2


def compare_iters(it1, it2):
    for i1, i2 in itertools.zip_longest(it1, it2):
        if i1 is None and i1 == i2:
            continue
        else:
            assert_equal_not_none(i1, i2)
