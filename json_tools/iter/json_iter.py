from typing import Dict
from typing import IO
from typing import Iterable
from typing import Union

from json_tools import jsonlib


def dump(fp: IO, data: Union[Dict,Iterable]):
    """ Dump array to a file object.

    Parameters
    ----------
    fp :
        File object to write to. Must be writable.
    data :
        Iterable object to write.
    """
    if isinstance(data, dict):
        fp.write(jsonlib.dumps(data))
        return

    fp.write('[\n')
    it = iter(data)
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


def load(fp: IO):
    data = jsonlib.load(fp)
    if isinstance(data, list):
        for obj in data:
            yield obj
    else:
        return data


def dump_array(filename, gen):
    with open(filename, 'w') as fp:
        return dump(fp, gen)

if __name__ == '__main__':
    import sys
    data = [{'a':1},{'a':2}]
    dump_array_json(sys.stdout, data)
