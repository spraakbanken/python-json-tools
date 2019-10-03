""" Handle JSON lazy. """
from typing import Dict
from typing import IO
from typing import Iterable
from typing import Union

import codecs

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
    if isinstance(fp.read(0), bytes):
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
    # return
    # # Determine type of data
    # c = fp.read(1)
    # if c != '[':
    #     fp.seek(0)
    #     print("json_iter.load: use jsonlib.")
    #     yield jsonlib.load(fp)
    # else:
    #     fp.seek(0)
    #     print("json_iter.load: use ijson.")
    #     yield from ijson.items(fp, 'item')
        # balance = 0
        # start_idx = None
        # chunk_size = 0
        # while True:
        #     curr_idx = fp.tell()
        #     c = fp.read(1)
        #     # print(f'c = {c}')
        #     if not c:
        #         # print('End of file')

        #         break
        #     # chunk_size += 1
        #     if c == '{':
        #         balance += 1
        #         if balance == 1:
        #             chunk_size = 1
        #             start_idx = curr_idx
        #     elif c == '}':
        #         balance -= 1

        #         if balance == 0:
        #             fp.seek(start_idx)
        #             chunk = fp.read(chunk_size)
        #             # print(f'read chunk "{chunk}"')
        #             yield jsonlib.loads(chunk)
        #             chunk_size = 0

        #     chunk_size += 1

        # # print(f"balance = {balance}")
        # # print(f"start_idx = {start_idx}")
        # # print(f"chunk_size = {chunk_size}")
        # if not start_idx:
        #     fp.seek(0)
        #     json_data = jsonlib.load(fp)
        #     if isinstance(json_data, list):
        #         for json_obj in json_data:
        #             yield json_obj
        #     else:
        #         yield json_data


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
        file_mode = "bw"
    with open(file_name, file_mode) as fp:
        return dump(gen, fp)
