try:
    from ujson import dump, dumps, load, loads
except ModuleNotFoundError:
    from json import dump, dumps, load, loads


def load_from_file(filename: str, *, mode='r', **kw):
    with open(filename, mode) as fp:
        return load(fp, **kw)


def dump_to_file(obj, filename: str, *, mode='w', **kw):
    with open(filename, mode) as fp:
        dump(obj, fp, **kw)

