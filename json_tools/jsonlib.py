try:
    from ujson import dump, dumps, load, loads  # noqa: F401
except ImportError:
    from json import dump, dumps, load, loads  # noqa: F401
