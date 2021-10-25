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
        super().__init__(id)  #Calling superClass id attribute

    @property
    def width(self):
        """Width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setters"""
        self.__width = value

    @property
    def height(self):
        """Height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """Height setters"""
        self.__height = value

    @property
    def x(self):
        """X getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setters"""
        self.__x = value

    @property
    def y(self):
        """Y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """Y setters"""
        self.__y = value
