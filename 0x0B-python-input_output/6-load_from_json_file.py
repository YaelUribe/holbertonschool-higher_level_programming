#!/usr/bin/python3
"""
Module: load_from_json_file
"""
import json


def load_from_json_file(filename):
    """ Function to create an object
    from a 'JSON file'"""
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
