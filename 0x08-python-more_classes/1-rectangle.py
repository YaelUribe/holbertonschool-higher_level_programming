#!/usr/bin/python3
"""Class Rectangle"""


class Rectangle:
    """Rectangle Class attributes and methods"""
    def __init__(self, width=0, height=0):
        """Defining private attributes"""
        if type(width) != int:
            raise ValueError("width must be an integer")
        elif width < 0:
            raise TypeError("width must be >= 0")
        if type(height) != int:
            raise ValueError("width must be an integer")
        elif height < 0:
            raise TypeError("width must be >= 0")
        self.width = width
        self.height = height

    @property
    def width(self):
        """caca"""
        return self.__width

    @width.setter
    def width(self, value):
        """caca"""
        if type(value) != int:
            raise ValueError("width must be an integer")
        elif value < 0:
            raise TypeError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """caca"""
        return self.__height

    @height.setter
    def height(self, value):
        """caca"""
        if type(value) != int:
            raise ValueError("height must be an integer")
        elif value < 0:
            raise TypeError("height must be >= 0")
        self.__height = value
