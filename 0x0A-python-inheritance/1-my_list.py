#!/usr/bin/python3
"""
Module - Mylist class
"""


class MyList(list):
    """Defining inheriting class Mylist """
    def print_sorted(self):
        """method to print the sorted list"""
        print(sorted(self))
