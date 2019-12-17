import json
import sys


def get_dict(filename):
    with open(filename) as fp:
        data = json.load(fp)

    result = {}
    for _id, doc in enumerate(data):
        result[_id] = doc

    return result


@profile
def update_plain_json(filename, with_id=True):
    data = get_dict(filename)

    if with_id:
        out = [{"_id": _id, "_source": doc} for _id, doc in data.items()]
    else:
        out = [doc for doc in data.values()]

    with open(f"{filename}.copy_w_json.json", "w") as fp:
        json.dump(out, fp)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = "benches/data/skbl.json"
    update_plain_json(filename)

