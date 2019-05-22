import os
from typing import Iterable
from typing import IO

from jt_iter import json_iter
from jt_iter import jsonl_iter


def _is_jsonl(p: str):
    root, suffix = os.path.splitext(p)
    # print('suffix = {suffix}'.format(suffix=suffix))
    return suffix in ['.jsonl']


def load(
    fp: IO,
    *,
    file_type=None
) -> Iterable:
    _iter = json_iter
    if file_type == 'json':
        pass
    elif file_type == 'jsonl':
        _iter = jsonl_iter
    else:
        if _is_jsonl(fp.name):
            _iter = jsonl_iter

    yield from _iter.load(fp)


def load_from_file(
        filename: str,
        *,
        filetype=None
        ):
    _iter = json_iter
    if filetype == 'json':
        pass
    elif filetype == 'jsonl':
        _iter = jsonl_iter
    else:
        if _is_jsonl(filename):
            _iter = jsonl_iter

    yield from _iter.load_from_file(filename)


def dump(
        in_iter_,
        fp: IO,
        *,
        filetype=None
        ):
    _iter = json_iter
    if filetype == 'json':
        pass
    elif filetype == 'jsonl':
        _iter = jsonl_iter
    else:
        if _is_jsonl(fp.name):
            _iter = jsonl_iter

    _iter.dump(in_iter_, fp)


def dump_to_file(
        in_iter_,
        filename: str,
        *,
        filetype=None
        ):
    _iter = json_iter
    if filetype == 'json':
        pass
    elif filetype == 'jsonl':
        _iter = jsonl_iter
    else:
        if _is_jsonl(filename):
            _iter = jsonl_iter

    _iter.dump_to_file(in_iter_, filename)


if __name__ == '__main__':
    files = [
        'tests/data/dict.json',
        'tests/data/array.json',
        'tests/data/array.jsonl',
    ]

    for f in files:
        print('reading {f} ...'.format(f=f))
        for i, o in enumerate(load_from_file(f)):
            print('{i}: {o}'.format(i=i, o=o))
