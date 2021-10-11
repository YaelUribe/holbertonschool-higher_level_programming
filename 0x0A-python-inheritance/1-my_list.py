#!/usr/bin/python3
"""
Class Mylist
"""


class Mylist(list):
    """Defining inheriting class Mylist """
    def print_sorted(self):
        """method to print the sorted list"""
        print(self.sort())
