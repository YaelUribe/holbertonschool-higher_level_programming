#!/usr/bin/python3
"""
Module - write_file
"""


def write_file(filename="", text=""):
    """ Function to write a string to a text file"""
    with open(filename, 'a' or 'x', encoding="utf-8") as f:
        print(f.write(text))
