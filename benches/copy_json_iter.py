import json
import sys
from sb_json_tools import json_iter


def get_dict(filename):
    with open(filename) as fp:
        data = json.load(fp)

    result = {}
    for _id, doc in enumerate(data):
        result[_id] = doc

    return result


@profile
def copy_json_iter(filename, with_id=False):
    data = get_dict(filename)

    if with_id:
        out = ({"_id": _id, "_source": doc} for _id, doc in data.itemss())
    else:
        out = (doc for doc in data.values())

    json_iter.dump_to_file(out, f"{filename}.copy_w_json_iter.json")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = "benches/data/skbl.json"
    update_plain_json(filename)

