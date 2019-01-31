def f(doc):
    r = doc.copy()
    r['b'] = 'b'
    return r


def test_dict():
    a = {'a': 'a'}
    b = f(a)
    assert 'b' in b
    assert 'b' not in a
