#!/usr/bin/python3
"""
module is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """Function to define if obj is instance
        of a_class or from a class inherited
        from
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
