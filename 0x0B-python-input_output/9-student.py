#!/usr/bin/python3
"""
Module: student.py
"""


class Student():
    """Class Student"""
    def __init__(self, first_name, last_name, age):
        """ instantiation for class Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Method to retrieve a dictionary representation
        of a Student instance
        """
        return self.__dict__
