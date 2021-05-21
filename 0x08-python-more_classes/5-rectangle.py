#!/usr/bin/python3
"""Class Rectangle"""


class Rectangle:
    """Rectangle Class attributes and methods"""
    def __init__(self, width=0, height=0):
        """Defining private attributes"""
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Method to determine area of our rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Method to determine perimeter of our rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return self.__width * 2 + self.__height * 2

    def __str__(self):
        "Returns class objects as a string "
        nu_string = ""
        if self.__width == 0 or self.__height == 0:
            return ""
        for y in range(self.__height):
            for x in range(self.__width):
                nu_string += "#"
            if y == self.__height - 1:
                break
            nu_string += "\n"
        return nu_string

    def __repr__(self):
        """Defining repr to print a string representation
        of the triangle"""
        return "Rectangle(" + str(self.__width) + ", "\
            + str(self.__height) + ")"

    def __del__(self):
        """Destructor of objects"""
        print("Bye rectangle...")
