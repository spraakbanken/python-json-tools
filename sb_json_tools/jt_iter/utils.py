import os


def is_jsonl(p: str):
    root, suffix = os.path.splitext(p)
    # print('suffix = {suffix}'.format(suffix=suffix))
    return suffix in ['.jsonl']
