#!/usr/bin/python3
"""Class Rectangle"""


class Rectangle:
    """Class rectangle instantiation"""
    def __init__(self, width=0, height=0):
        """Private attributes"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """width properties"""
        return self.__width

    @property
    """height properties"""
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        """"Set width properties"""
        self.__width = value
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")

    @height.setter
    def height(self, value):
        """set height properties"""
        self.__height = value
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
