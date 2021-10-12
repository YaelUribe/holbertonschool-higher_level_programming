#!/usr/bin/python3
"""
Module: append_write
"""


def append_write(filename="", text=""):
    """ Function to blah blah UTF8"""
    with open(filename, 'a', encoding="utf8") as f:
        return f.write(text)
