#!/usr/bin/python3
"""
Module: append_write
"""


def append_write(filename="", text=""):
    with open(filename, 'a', encoding="utf8") as f:
        f.write(text)
        return len(text)
