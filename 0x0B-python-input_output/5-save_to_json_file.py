#!/usr/bin/python3
"""
Module:save_to_json_file
"""
import json


def save_to_json_file(my_obj, filename):
    """ Function to write an object to a
    text file, from JSON representation"""
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
