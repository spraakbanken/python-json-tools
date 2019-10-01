from sb_json_tools import jt_val as jv


schema = {
    "type": "object",
    "properties": {
        "valid": {
            "type": "integer"
        }
    },
    "required": ["valid"]
}


def gen_valid_data(n):
    for i in range(n):
        yield {'valid': i}


def gen_invalid_data(n):
    for i in range(n):
        yield {'invalid': i}


def gen_mixed_data(n):
    for i in range(n):
        if i % 2 == 1:
            yield {'valid': i}
        else:
            yield {'invalid': i}


def test_valid_data():
    n = 10
    stream = jv.streaming_validate(schema, gen_valid_data(n))

    for i, (ok, error) in enumerate(stream):
        assert ok
        assert ok['valid'] == i
        assert not error


def test_invalid_data():
    n = 10
    stream = jv.streaming_validate(schema, gen_invalid_data(n))
    for ok, error in stream:
        assert error
        assert not ok


def test_mixed_data():
    n = 10
    stream = jv.streaming_validate(schema, gen_mixed_data(n))
    for i, (ok, error) in enumerate(stream):
        if i % 2 == 1:
            assert ok
            assert not error
        else:
            assert error
            assert not ok
