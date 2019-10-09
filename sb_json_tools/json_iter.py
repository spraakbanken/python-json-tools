""" Handle JSON lazy. """
from typing import Dict
from typing import IO
from typing import Iterable
from typing import Union

import codecs
import io

import ijson

from sb_json_tools import jsonlib


def dump(data: Union[Dict, Iterable], fp: IO):
    """ Dump array to a file object.

    Parameters
    ----------
    fp :
        File object to write to. Must be writable.
    data :
        Iterable object to write.
    """
    if isinstance(fp, io.BufferedIOBase):
        fp = codecs.getwriter('utf-8')(fp)

    if isinstance(data, dict):
        fp.write(jsonlib.dumps(data))
        return

    try:
        it = iter(data)
    except TypeError:
        fp.write(jsonlib.dumps(data))
        return

    fp.write('[\n')
    try:
        obj = next(it)
        fp.write(jsonlib.dumps(obj))
    except StopIteration:
        pass
    else:
        for v in it:
            fp.write(',\n')
            fp.write(jsonlib.dumps(v))
    fp.write('\n]')


def load(fp: IO) -> Iterable:
    yield from ijson.items(fp, 'item')


def load_eager(fp: IO):
    data = jsonlib.load(fp)
    if isinstance(data, list):
        for obj in data:
            yield obj
    else:
        return data


def load_from_file(file_name: str, *, file_mode: str = None):
    if not file_mode:
        file_mode = "br"
    with open(file_name, file_mode) as fp:
        yield from load(fp)


def dump_to_file(gen: Iterable, file_name: str, *, file_mode: str = None):
    if not file_mode:
        file_mode = "w"
    with open(file_name, file_mode) as fp:
        return dump(gen, fp)
