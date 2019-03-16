from typing import IO
from typing import Iterable

from json_tools import jsonlib


def dump_array_json(stream: IO, data: Iterable):
    """ Dump array to a file object.

    Parameters
    ----------
    fp : file object
        File object to write to. Must be writable.
    gen : Iterable
        Iterable object to write.
    """
    stream.write('[\n')
    it = iter(data)
    try:
        obj = next(it)
        stream.write(jsonlib.dumps(obj))
    except StopIteration:
        pass
    else:
        for v in it:
            stream.write(',\n')
            stream.write(jsonlib.dumps(v))
    stream.write('\n]')


def dump_array(filename, gen):
    with open(filename, 'w') as fp:
        return dump_array_json(fp, gen)

if __name__ == '__main__':
    import sys
    data = [{'a':1},{'a':2}]
    dump_array_json(sys.stdout, data)
