"""Common test functions."""
import decimal
import itertools
import math

# import decimal
from string import printable

from hypothesis import strategies as st

from json_streams import jsonlib

JSON_DATA = st.recursive(
    st.none()
    | st.booleans()
    | st.floats(allow_nan=False, allow_infinity=False)
    | st.integers()
    | st.text(printable),
    lambda children: st.lists(children, 1).filter(lambda l: len(l) > 1 or l[0] is None)
    | st.dictionaries(
        st.text(printable).filter(lambda s: len(s) > 0), children, min_size=1
    ),
)


def reference_dict(x):
    """Create a reference dict for testing.

    Arguments:
        x {any} -- the object to make a reference object

    Returns:
        any -- the reference version
    """
    return jsonlib.loads(
        jsonlib.dumps(x, **jsonlib.JSON_SETTINGS), **jsonlib.JSON_SETTINGS
    )


def convert_to_decimal_if_float(x):
    """Convert value to float to Decimal.

    Arguments:
        x {any} -- The value to test and convet if float.

    Returns:
        any -- Decimal if x is a float, otherwise x
    """
    if isinstance(x, float):
        return decimal.Decimal(x)
    else:
        return x


def assert_equal_not_none(i1, i2):
    """Assert to objects are equal and no one is None.

    Arguments:
        i1 {any} -- first object
        i2 {any} -- second object
    """
    assert i1 is not None
    assert i2 is not None
    if isinstance(i1, (decimal.Decimal, float)):
        assert math.isclose(i1, i2)
    else:
        assert i1 == i2


def compare_iters(it1, it2):
    """Compare two iterables with asserts.

    Arguments:
        it1 {Iterable} -- first iterable
        it2 {Iterable} -- second iterable
    """
    for i1, i2 in itertools.zip_longest(it1, it2):
        if i1 is None and i1 == i2:
            continue
        else:
            if isinstance(i1, list) and isinstance(i2, list):
                compare_iters(i1, i2)
            else:
                assert_equal_not_none(i1, i2)
