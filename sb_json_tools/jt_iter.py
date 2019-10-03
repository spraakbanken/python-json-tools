from typing import Iterable
from typing import IO

from . import json_iter
from . import jsonl_iter
from . import utils


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
        if utils.is_jsonl(fp.name):
            _iter = jsonl_iter

    yield from _iter.load(fp)


def load_from_file(
        file_name: str,
        *,
        file_type: str = None,
        file_mode: str = None
        ):
    _iter = json_iter
    if file_type == 'json':
        pass
    elif file_type == 'jsonl':
        _iter = jsonl_iter
    else:
        if utils.is_jsonl(file_name):
            _iter = jsonl_iter

    yield from _iter.load_from_file(file_name, file_mode=file_mode)


def dump(
        in_iter_,
        fp: IO,
        *,
        file_type: str = None
        ):
    _iter = json_iter
    if file_type == 'json':
        pass
    elif file_type == 'jsonl':
        _iter = jsonl_iter
    else:
        if utils.is_jsonl(fp.name):
            _iter = jsonl_iter

    _iter.dump(in_iter_, fp)


def dump_to_file(
        in_iter_,
        file_name: str,
        *,
        file_type=None,
        file_mode: str = None
):
    _iter = json_iter
    if file_type == 'json':
        pass
    elif file_type == 'jsonl':
        _iter = jsonl_iter
    else:
        if utils.is_jsonl(file_name):
            _iter = jsonl_iter

    _iter.dump_to_file(in_iter_, file_name, file_mode=file_mode)
