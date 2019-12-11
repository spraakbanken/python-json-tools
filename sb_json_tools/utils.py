"""Util functions.
"""
import os


def is_jsonl(name: str) -> bool:
    """Test if a filename is json lines.
    Also returns True for '<stdin>' and '<stdout>'.

    Arguments:
        name {str} -- name to test

    Returns:
        {bool} -- True if this name is jsonl.
    """
    if name in ["<stdin>", "<stdout>"]:
        return True
    _, suffix = os.path.splitext(name)
    # print('suffix = {suffix}'.format(suffix=suffix))
    return suffix in [".jsonl"]
