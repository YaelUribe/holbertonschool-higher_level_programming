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

    def to_json(self, attrs=None):
        """
        Method to retrieve a dictionary representation
        of a Student instance
        """
        if attrs is None:
            return self.__dict__

        ndict = {}
        for i in attrs:
            try:
                ndict[i] = self.__dict__[i]
            except:
                pass
        return ndict
