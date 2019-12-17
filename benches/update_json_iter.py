import sys

from sb_json_tools import json_iter


def update_obj(obj):
    obj["updated"] = True
    return obj


@profile
def update_json_iter(filename):
    data = json_iter.load_from_file(filename)

    updated_data = (update_obj(obj)
                    for obj in data)

    json_iter.dump_to_file(updated_data, f"{filename}.updated_w_json_iter.json")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = "benches/data/skbl.json"
    update_plain_json(filename)

