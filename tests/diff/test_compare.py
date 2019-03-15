from json_tools import diff

dict1 = {
	'a': 1
}


def test_same_diff():
	result = diff.compare(dict1, dict1)
	assert len(result) == 0
