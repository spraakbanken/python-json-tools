""" Use JSON with generators. """

from typing import IO, Dict, Iterable, Union

from json_tools import jsonlib


def dump(data: Union[Dict, Iterable], fp: IO, **kw):
    """ Dump array to a file object.

    Parameters
    ----------
    fp :
        File object to write to. Must be writable.
    data :
        Iterable object to write.
    **kw :
        keyword arguments to jsonlib
    """
    if isinstance(data, dict):
        jsonlib.dump(data, fp, **kw)
        return

    fp.write("[\n")
    it = iter(data)
    try:
        obj = next(it)
        fp.write(jsonlib.dumps(obj, **kw))
    except StopIteration:
        pass
    else:
        for v in it:
            fp.write(",\n")
            fp.write(jsonlib.dumps(v, **kw))
    fp.write("\n]")


def load(fp: IO, **kw):
    """ Load JSON and generate objects in arrays. """
    data = jsonlib.load(fp, **kw)
    if isinstance(data, list):
        for obj in data:
            yield obj
    else:
        return data


def dump_to_file(gen, filename: str, *, file_mode="w", **kw):
    with open(filename, file_mode) as fp:
        dump(gen, fp, **kw)


def load_from_file(filename: str, *, file_mode="r", **kw):
    with open(filename, file_mode) as fp:
        return load(fp, **kw)


if __name__ == "__main__":
    import sys

    data = [{"a": 1}, {"a": 2}]
    dump_to_file(data, sys.stdout)
