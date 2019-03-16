from json_tools import val as jv


schema = {
    "type": "object",
    "properties": {
        "valid" : {
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
    
    for i, result in enumerate(stream): 
        assert result.ok
        assert result.ok['valid'] == i
        assert not result.error


def test_invalid_data():
    n = 10
    stream = jv.streaming_validate(schema, gen_invalid_data(n))
    for result in stream:
        assert result.error
        assert not result.ok


def test_mixed_data():
    n = 10
    stream = jv.streaming_validate(schema, gen_mixed_data(n))
    for i, result in enumerate(stream):
        if i % 2 == 1:
            assert result.ok
            assert not result.error
        else:
            assert result.error
            assert not result.ok
    