#!/usr/bin/python3
"""Class to define a Square"""


class Square:
    """Class Square"""
    def __init__(self, size=0):
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Public Method to calculate area of a Square"""
        self.__size *= self.__size
        return self.__size
