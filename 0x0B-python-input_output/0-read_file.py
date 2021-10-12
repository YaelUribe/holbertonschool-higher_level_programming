#!/usr/bin/python3
"""
Module - read_file
"""


def read_file(filename=""):
    """Read file method, to stdout from utf-8 encoding"""
    with open(filename, 'r', encoding="utf8") as f:
        print(f.read())
