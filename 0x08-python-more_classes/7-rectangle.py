#!/usr/bin/python3
"""Class Rectangle"""


class Rectangle:
    """Class rectangle instantiation"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Private attributes"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """area of a rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """perimeter of a rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return Class objects as strings"""
        new = ""
        if self.__height == 0 or self.__width == 0:
            return ""
        for h in range(self.__height):
            for w in range(self.__width):
                new += str(self.print_symbol)
            if h == self.__height - 1:
                break
            new += "\n"
        return new

    def __repr__(self):
        """__repr__ to print a string representation of a rectangle"""
        return "Rectangle(" + str(self.__width) + ", "\
            + str(self.__height) + ")"

    def __del__(self):
        """Object destructor, when using del()"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
