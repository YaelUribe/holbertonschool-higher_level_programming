#!/usr/bin/python3
"""Square Class to define a square"""


class Square:
    """Class: Square"""
    def __init__(self, size=0):
        """Defining private attributes"""
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
