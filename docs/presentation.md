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
