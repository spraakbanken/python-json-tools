from typing import IO
from typing import Iterable

from json_tools import jsonlib


def dump_array_jsonl(stream: IO, data: Iterable):
    for it in data:
        stream.write(jsonlib.dumps(it))
        stream.write('\n')

if __name__ == '__main__':
    import sys
    data = [{'a':1},{'a':2}]
    dump_array_jsonl(sys.stdout, data)
