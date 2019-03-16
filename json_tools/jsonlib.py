try:
    from ujson import dump, dumps, load, loads
except ModuleNotFoundError:
    from json import dump, dumps, load, loads
