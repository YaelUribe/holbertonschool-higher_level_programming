#!/usr/bin/python3
"""
module inherits_from
"""


def inherits_from(obj, a_class):
    """Function to define if obj is instance
        of a class that inherited directly
        or indirectly from a_class
    """
    if isinstance(obj, a_class):
        if type(obj) is not a_class:
            return True
    else:
        return False
