import json_validator as jv


schema = {
    "type": "object",
    "properties": {
        "int": {
            "type": "integer"
        },
        "num": {
            "type": "number"
        }
    },
    "required": ["int", "num"]
}


valid_data = [
    {"int": 1, "num": 3.4},
    {"int": 2.0, "num": 3.4},
    {"int": 2, "num": 4}
]


invalid_data = [
    {"int": 2.5, "num": 5.6}
]


def test_valid_data():
    for result in jv.streaming_validate(schema, valid_data):
        assert result.ok is not None
        assert result.error is None


def test_invalid_data():
    for result in jv.streaming_validate(schema, invalid_data):
        assert result.ok is None
        assert result.error is not None
