import json
import sys


@profile
def update_plain_json(filename):
    with open(filename) as fp:
        data = json.load(fp)

    for obj in data:
        obj["updated"] = True

    with open(f"{filename}.updated_w_json.json", "w") as fp:
        json.dump(data, fp)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = "benches/data/skbl.json"
    update_plain_json(filename)

