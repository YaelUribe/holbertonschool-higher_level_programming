#!/usr/bin/python3
"""
Module: fom_json_string
"""
import json


def from_json_string(my_str):
    """Function to return the JSON
    representation of an object (string)"""
    return json.loads(my_str)
