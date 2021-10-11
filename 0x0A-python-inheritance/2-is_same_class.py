#!/usr/bin/python3
"""
module is_same_class
"""


def is_same_class(obj, a_class):
    """Function to define if obj is exactly instance
        of a_class
    """
    if type(obj) is a_class:
        return True
    else:
        return False
