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

    def area(self):
        """Method to calculate area"""
        return self.__size * self.__size

    def my_print(self):
        """Printing to stdout with # char"""
        if self.__size != 0:
            for columns in range(self.__size):
                for rows in range(self.__size):
                    print("#", end="")
                print()
        else:
            print()

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
