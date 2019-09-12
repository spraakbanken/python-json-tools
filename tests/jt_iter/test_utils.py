from jt_iter.utils import is_jsonl


def test_jsonl():
    filename = "test.jsonl"
    assert is_jsonl(filename)


def test_json():
    filename = "test.json"
    assert not is_jsonl(filename)
