#!/usr/bin/python3
"""Class Rectangle"""


class Rectangle:
    """Rectangle Class attributes and methods"""
    def __init__(self, width=0, height=0):
        """Defining private attributes"""
        self.width = width
        self.height = height

    @property
    def height(self):
        """caca"""
        return self.__height

    @height.setter
    def height(self, value):
        """caca"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """caca"""
        return self.__width

    @width.setter
    def width(self, value):
        """caca"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
