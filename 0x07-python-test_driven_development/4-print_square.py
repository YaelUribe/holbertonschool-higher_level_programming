#!/usr/bin/python3
"""
print_square module:
Function to print a square
"""


def print_square(size):
    """
    Function to print a Square
    Parameters:
    -----------
    size : size length of the square
    return
    -----------
    Returns the figure of the square using "#" character
    """
    # verify size is int or positive float
    if type(size) is float:
        if size < 0:
            raise TypeError("size must be an integer")
        size = int(size)
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    # Now let's print our square
    for base in range(size):
        for height in range(size):
            print("#", end="")
        print()
