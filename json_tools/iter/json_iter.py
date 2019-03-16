from typing import Dict
from typing import IO
from typing import Iterable
from typing import Union

from json_tools import jsonlib


def dump(stream: IO, data: Union[Dict,Iterable]):
    """ Dump array to a file object.

    Parameters
    ----------
    fp :
        File object to write to. Must be writable.
    data :
        Iterable object to write.
    """
    if isinstance(data, dict):
        stream.write(jsonlib.dumps(data))
        return
    
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
