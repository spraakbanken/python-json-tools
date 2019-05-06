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
    # Determine type of data
    c = fp.read(1)
    if c != '[':
        fp.seek(0)
        yield jsonlib.load(fp)
    else:
        balance = 0
        start_idx = None
        chunk_size = 0
        found_obj = False
        while True:
            curr_idx = fp.tell()
            c = fp.read(1)
            # print(f'c = {c}')
            if not c:
                # print('End of file')

                break
            # chunk_size += 1
            if c == '{':
                found_obj = True
                balance += 1
                if balance == 1:
                    chunk_size = 1
                    start_idx = curr_idx
            elif c == '}':
                balance -= 1

            if found_obj and balance == 0:
                fp.seek(start_idx)
                chunk = fp.read(chunk_size)
                # print(f'read chunk {chunk}')
                yield jsonlib.loads(chunk)
                chunk_size = 0
                found_obj = False
            else:
                chunk_size += 1

def load_eager(fp: IO):
    data = jsonlib.load(fp)
    if isinstance(data, list):
        for obj in data:
            yield obj
    else:
        return data


def load_from_file(filename: str):
    with open(filename, 'r') as fp:
        yield from load(fp)


def dump_to_file(filename, gen):
    with open(filename, 'w') as fp:
        return dump(fp, gen)



def main():
    files = [
        'tests/data/dict.json',
        'tests/data/array.json',
    ]

    for f in files:
        print(f'Reading {f} ...')
        for obj in load_from_file(f):
            print(f'obj = {obj}')
        print('')

if __name__ == '__main__':
    import sys
    data = [{'a':1},{'a':2}]
    dump(sys.stdout, data)

    main()

