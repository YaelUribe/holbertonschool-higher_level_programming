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

    @width.setter
    def width(self, value):
        """"Set width properties"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height properties"""
        return self.__height

    @height.setter
    def height(self, value):
        """set height properties"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
