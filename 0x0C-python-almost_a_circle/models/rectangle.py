#!/usr/bin/python3
"""
Module: Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """
    Class rectangle that inherits from Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)  # Calling superClass id attribute

    @property
    def width(self):
        """Width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setters"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """Height setters"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """X getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setters"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """Y setters"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Area public method"""
        return self.width * self.height

    def display(self):
        """Function to print in STDOUT
        rectangle instance with "#" Character"""
        space = self.x
        nuline = self.y
        if nuline != 0:
            print('\n' * (nuline - 1))
        for g in range(self.height):
            print(" "*space + "#"*self.width)

    def __str__(self):
        """prints the requested message"""
        return("[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}").format(self.id,
                                                                  self.x,
                                                                  self.y,
                                                                  self.width,
                                                                  self.height)
