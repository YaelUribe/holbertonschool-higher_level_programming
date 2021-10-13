#!/usr/bin/python3
"""
Module: class_to_json
"""
import json


def class_to_json(obj):
    """
    Function to return the dictionary description with
    simple data structure for JSON serialization of an object
    """
    return obj.__dict__
