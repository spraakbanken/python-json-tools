from typing import Dict
from typing import IO
from typing import Iterable
from typing import Union

from json_tools import jsonlib


def dump(data: Union[Dict, Iterable], fp: IO):
    if isinstance(data, dict):
        fp.write(jsonlib.dumps(data))
        fp.write('\n')
        return
    for it in data:
        fp.write(jsonlib.dumps(it))
        fp.write('\n')


def load(fp: IO) -> Iterable:
    for line in fp:
        yield jsonlib.loads(line)


if __name__ == '__main__':
    import sys
    data = [{'a':1},{'a':2}]
    dump(sys.stdout, data)
