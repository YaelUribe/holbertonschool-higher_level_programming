#!/usr/bin/python3
"""Square Class to define a square"""


class Square:
    """Class: Square and its methods"""
    def __init__(self, size=0, position=(0, 0)):
        """Defining private attributes and their conditions"""
        self.__size = size
        self.__position = position
        if type(self.__size) is not int:
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")
        if type(position) is not tuple or (len(position) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        for idx in position:
            if idx < 0 or type(idx) is not int:
                raise TypeError("position must be a tuple of 2 \
                     positive integers")

    def area(self):
        """Method to calculate area"""
        return self.__size * self.__size

    def my_print(self):
        """Printing to stdout with # char"""
        if self.__size != 0:
            for tup_0 in range(self.__position[1]):
                print()
            for columns in range(self.__size):
                for tup_1 in range(self.__position[0]):
                    print(" ", end="")
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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        self.__position = value
        if type(value) is not tuple or (len(value) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        for idx in value:
            if idx < 0 or type(idx) is not int:
                raise TypeError("position must be a tuple of 2\
                     positive integers")
