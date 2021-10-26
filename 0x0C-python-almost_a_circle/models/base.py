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
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Class Method save_to_file
        writes the JSON str repr of list_objs
        to a file
        """
        filename = str(cls.__name__) + ".json"
        nuJson = []
        with open(filename, 'w', encoding='utf8') as f:
            if list_objs is None:
                f.write("[]")
            else:
                for x in list_objs:
                    nuJson.append(x.to_dictionary())
                f.write(cls.to_json_string(nuJson))

    @staticmethod
    def from_json_string(json_string):
        """
        StaticMethod to return the list of JSON str repr
        """
        if json_string is None:
            return []
        else:
            return json.loads(json_string)
