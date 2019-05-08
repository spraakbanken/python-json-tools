try:
    from ujson import dump, dumps, load, loads  # noqa: F401
except ImportError:
    from json import dump, dumps, load, loads  # noqa: F401


def load_from_file(filename: str):
    with open(filename, 'r') as fp:
        return load(fp)


def dump_to_file(obj, filename: str):
    with open(filename, 'w') as fp:
        return dump(obj, fp)
