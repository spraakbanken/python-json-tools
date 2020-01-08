# sb-json-tools

## Kristoffer Andersson

---

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

```
python -m memory_profiler benches/copy_plain_json.py tests/data/npegl_eng.json
```

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

Great! But then someone needs that output in [JSON Lines](http://jsonlines.org/)...

---

# Aside: JSON Lines

```
    JSON            |   JSON Lines
[                   |   {"a": 1}
    {"a": 1},       |   {"a": 2}
    {"a": 2}        |
]                   |
```

---

But that is really simple:

```
def dump(data, fp):
    for obj in data:
        fp.write(jsonlib.dumps(obj))
        fp.write('\n')
```

## So now we can write `jsonl_iter.dump(out, fp)

But wait, what about that memory copy:

````
python -m memory_profiler benches/copy_plain_json.py tests/data/npegl_eng.json
Filename: benches/copy_plain_json.py

Line #    Mem usage    Increment   Line Contents
================================================
    16   14.426 MiB   14.426 MiB   @profile
    17                             def copy_plain_json(filename, with_id=True):
    18 2534.949 MiB 2520.523 MiB       data = get_dict(filename)
    19
    20 2534.949 MiB    0.000 MiB       if with_id:
    21 2654.027 MiB    0.258 MiB           out = [{"_id": _id, "_source": doc} for _id, doc in data.items()]
    22                                 else:
    23                                     out = [doc for doc in data.values()]
    24
    25 2654.027 MiB    0.000 MiB       with open(f"{filename}.copy_w_json.json", "w") as fp:
    26                                     json.dump(out, fp)```
````

````
python -m memory_profiler benches/copy_json_iter.py tests/data/npegl_eng.json                                                   1   press
Filename: benches/copy_json_iter.py

Line #    Mem usage    Increment   Line Contents
================================================
    17   15.336 MiB   15.336 MiB   @profile
    18                             def update_plain_json(filename, with_id=False):
    19 2535.945 MiB 2520.609 MiB       data = get_dict(filename)
    20
    21 2535.945 MiB    0.000 MiB       if with_id:
    22                                     out = ({"_id": _id, "_source": doc} for _id, doc in data.itemss())
    23                                 else:
    24 2535.973 MiB    0.027 MiB           out = (doc for doc in data.values())
    25
    26 2535.973 MiB    0.000 MiB       json_iter.dump_to_file(out, f"{filename}.copy_w_json_iter.json")```

````

Ok, not so much gained.

Let's read a file with a generator...

---

We implement the following functions that returns generators:

```
json_iter.load(fp)
jsonl_iter.load(fp)
```

and macro functions to automagically choose between the iterators:

```
jt_iter.load(fp)
jt_iter.dump(fp)
```

and we can try them with, when implementing a length function:

```
@cli.command()
@click.argument("src", type=click.File("r"))
def length(src):
    for _len, _ in enumerate(jt_iter.load(src), 1):
        pass
    click.echo(_len)
```

Let's try it against [`jq`](https://stedolan.github.io/jq/) with `mprof` from [`memory-profiler`](https://pypi.org/project/memory-profiler/). Sample rate is 0.1 s.

```
                jq                              |               jt with json                                |           jt with ujson
mprof run jq 'length' benches/data/skbl.json    |   mprof run jt length benches/data/skbl.json              |   mprof run jt length benches/data/skbl.json
CMDLINE jq length benches/data/skbl.json        |   CMDLINE jt length benches/data/skbl.json                |   CMDLINE jt length benches/data/skbl.json
MEM 0.375000 1576571361.8905                    |   MEM 0.929688 1576571339.3044
MEM 25.511719 1576571361.9912                   |   MEM 16.050781 1576571339.4051
MEM 61.089844 1576571362.0921                   |   MEM 19.218750 1576571339.5055
                                                |   MEM 19.218750 1576571339.6061
                                                |   MEM 19.218750 1576571339.7071
                                                |                                                           |
Total runtime:      0.2016 s                    |   Total runtime:      0.4027 s                            |   Total runtime:      0 s
Max memory usage:   61 MB                       |   Max memory usage:   19 MB (including Python runtime)    |   Max memory usage:   0 MB (including Python runtime)
```

This JSON file is an array of size 1011 and takes 17 MB on disk.
So, `jq` is faster but `jt` uses less memory...

---

Let's give it something chunkier... A JSON file with 498,505 entries and 710 MB.

```
                jq                              |               jt with json                                |           jt with ujson
CMDLINE jq length tests/data/npegl_eng.json     |   CMDLINE jt length tests/data/npegl_eng.json             |   mprof run jt length tests/data/npegl_eng.json
MEM 1.230469 1576571397.9639                    |   MEM 0.921875 1576571426.3595                            |   CMDLINE jt length
MEM 23.792969 1576571398.0646                   |   MEM 18.105469 1576571426.4602
MEM 65.042969 1576571398.1653                   |   MEM 18.105469 1576571426.5610
MEM 104.488281 1576571398.2660                  |   MEM 18.105469 1576571426.6617
...
MEM 4796.304688 1576571414.9015
MEM 4402.324219 1576571415.0021
MEM 0.000000 1576571415.1029
                                                |                                                           |
Total runtime:      17.1390 s                   | Total runtime:        16.5235 s                           |   Total runtime:      0 s
Max memory usage:   4796 MB                     | Max memory usage:     18 MB (including Python runtime)    |   Max memory usage:   0 MB (including Python runtime)
```

This JSON file is an array of size 498505 and takes 710 MB on disk.
**Whow**, `jt` is both faster _and_ uses less memory than `jq`...

```
python -m memory_profiler benches/update_plain_json.py benches/data/data.json
Filename: benches/update_plain_json.py

# Line # Mem usage Increment Line Contents

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
