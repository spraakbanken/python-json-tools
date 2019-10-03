"""
Utility library to load the underlying json library.

Imports `ujson` if it is present, otherwise it imports `json` from
the standard library.
"""
try:
    from ujson import dump, dumps, load, loads  # pylint: disable=unused-import
except ImportError:
    from json import dump, dumps, load, loads  # noqa: F401


def load_from_file(filename: str):
    """
    Load the JSON file with the given filename.

    :param file_name: name of the file to load from.
    :return: the loaded JSON file.
    """
    with open(filename, 'r') as fp:
        return load(fp)


def dump_to_file(obj, filename: str):
    """
    Dump to a JSON file with the given file name.

    :param obj: the object to dump.
    :param file_name: name of the file to dump to.
    :return: anything returned from the backend.
    """
    with open(filename, 'w') as fp:
        return dump(obj, fp)
