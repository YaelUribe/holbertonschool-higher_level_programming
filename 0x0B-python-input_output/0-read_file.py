#!/usr/bin/python3
"""
Module - read_file
"""


def read_file(filename=""):
    """Read file method"""
    with open(filename) as f:
        f.read()
