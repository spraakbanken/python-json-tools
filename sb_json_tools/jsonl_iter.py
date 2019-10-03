from typing import Dict
from typing import IO
from typing import Iterable
from typing import Union

import codecs

from sb_json_tools import jsonlib


def dump(data: Union[Dict, Iterable], fp: IO):
    if isinstance(fp.read(0), bytes):
        fp = codecs.getwriter('utf-8')(fp)

    if isinstance(data, dict):
        fp.write(jsonlib.dumps(data))
        fp.write('\n')
        return

    try:
        for obj in data:
            fp.write(jsonlib.dumps(obj))
            fp.write('\n')
    except TypeError:
        fp.write(jsonlib.dumps(data))
        fp.write('\n')


def load(fp: IO) -> Iterable:
    for line in fp:
        yield jsonlib.loads(line)


def load_from_file(filename: str):
    with open(filename, 'r') as fp:
        yield from load(fp)


def dump_to_file(obj, filename):
    with open(filename, 'w') as fp:
        dump(obj, fp)
