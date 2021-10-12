#!/usr/bin/python3
"""
Module - write_file
"""


def write_file(filename="", text=""):
    """ Function to write a string to a text file"""
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
