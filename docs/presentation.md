# sb-json-tools
## Kristoffer Andersson

***

# Background

The idea of `sb-json-tools` began taking form after stumbling over this code
```
    entries = get_entries_to_save()

    if condition:
        out = [{"key": k, "val": v} for k, v in entries.items()]
    else:
        out = [v for v in entries.values()]

    json.dump(out, fp)
```

This code works, but sometimes you work with large data sets and that extra array starts keeping you awake.

What if we could generators instead?
```
    if condition:
        out = ({"key": k, "val": v} for k,v in entries.items())
    else:
        out = (v for v in entries.values())
```

Ok, so we removed that memory allocation, are we done?

No, since `json` doesn't handle generators...
```
Python 3.8.0 (default, Nov 20 2019, 20:44:46)
[Clang 8.0.7 (https://android.googlesource.com/toolchain/clang b55f2d4ebfd35bf6 on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> g = ("t" for _ in range(5))
>>> import json
>>> json.dumps(g)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/data/data/com.termux/files/usr/lib/python3.8/json/__init__.py", line 231, in dumps
    return _default_encoder.encode(obj)
  File "/data/data/com.termux/files/usr/lib/python3.8/json/encoder.py", line 199, in encode
    chunks = self.iterencode(o, _one_shot=True)
  File "/data/data/com.termux/files/usr/lib/python3.8/json/encoder.py", line 257, in iterencode
    return _iterencode(o, 0)
  File "/data/data/com.termux/files/usr/lib/python3.8/json/encoder.py", line 179, in default
    raise TypeError(f'Object of type {o.__class__.__name__} '
TypeError: Object of type generator is not JSON serializable

```
Bummer, let's create a small library so we can use generators.
```
    json_iter.dump(out, fp)
```

Great! But then someone needs that output in
```
python -m memory_profiler benches/update_plain_json.py benches/data/data.json
Filename: benches/update_plain_json.py

Line #    Mem usage    Increment   Line Contents
================================================
     5   14.395 MiB   14.395 MiB   @profile
     6                             def update_plain_json(filename):
     7   14.395 MiB    0.000 MiB       with open(filename) as fp:
     8   73.895 MiB   59.500 MiB           data = json.load(fp)
     9
    10   73.895 MiB    0.000 MiB       for obj in data:
    11   73.895 MiB    0.000 MiB           obj["updated"] = True
    12
    13   73.895 MiB    0.000 MiB       with open(f"{filename}.updated_w_json.json", "w") as fp:
    14   73.895 MiB    0.000 MiB           json.dump(data, fp)
```
>>>
