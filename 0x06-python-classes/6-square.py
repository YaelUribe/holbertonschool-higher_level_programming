#!/usr/bin/python3
"""Class to define a Square"""


class Square:
    """Class Square"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        elif type(position) is not tuple or (len(position) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        for index in position:
            if index < 0 or type(index) is not int:
                raise TypeError("position must be a tuple of\
                    2 positive integers")

    def area(self):
        """Public Method to calculate area of a Square"""
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, value):
        self.__size = value
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

    @position.setter
    def position(self, value):
        self.__position = value
        if (len(value) != 2) or type(value) is not tuple:
            raise TypeError("position must be a tuple of 2\
                positive integers")
        for index in value:
            if index < 0 or type(index) is not int:
                raise TypeError("position must be a tuple of\
                    2 positive integers")

    def my_print(self):
        """Public instance Method to print a Square"""
        if self.__size == 0:
            print()
        else:
            for tup0 in range(self.__position[1]):
                print()
            for x in range(self.__size):
                for tup1 in range(self.__position[0]):
                    print(" ", end="")
                for y in range(self.__size):
                    print("#", end="")
                print()
