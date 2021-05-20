#!/usr/bin/python3
"""Class Rectangle"""


class Rectangle:
    """Rectangle Class attributes and methods"""
    def __init__(self, width=0, height=0):
        """Defining private attributes"""
        self.__height = height
        self.__width = width
        if width < 0:
            raise TypeError("width must be >= 0")
        elif type(width) != int:
            raise ValueError("width must be an integer")
        if height < 0:
            raise TypeError("width must be >= 0")
        elif type(height) != int:
            raise ValueError("width must be an integer")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value
        if value < 0:
            raise TypeError("width must be >= 0")
        elif type(value) != int:
            raise ValueError("width must be an integer")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value
        if value < 0:
            raise TypeError("height must be >= 0")
        elif type(value) != int:
            raise ValueError("height must be an integer")