#!/usr/bin/python3
"""
Module: Base
"""
import json


class Base:
    """
    Class: Base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Base class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Public instance method to return JSON string
        repretsentation of list_dictionaries
        """
        if list_dictionaries is None:
            list_dictionaries = []
        else:
            return json.dumps(list_dictionaries)
