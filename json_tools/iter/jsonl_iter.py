from typing import Dict
from typing import IO
from typing import Iterable
from typing import Union

from json_tools import jsonlib


def dump(stream: IO, data: Union[Dict, Iterable]):
    if isinstance(data, dict):
        stream.write(jsonlib.dumps(data))
        stream.write('\n')
        return
    for it in data:
        stream.write(jsonlib.dumps(it))
        stream.write('\n')

if __name__ == '__main__':
    import sys
    data = [{'a':1},{'a':2}]
    dump(sys.stdout, data)
