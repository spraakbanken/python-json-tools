from sb_json_tools import jt_val as jv


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
    for ok, error in jv.streaming_validate(schema, valid_data):
        assert ok is not None
        assert error is None


def test_invalid_data():
    for ok, error in jv.streaming_validate(schema, invalid_data):
        assert ok is None
        assert error is not None
