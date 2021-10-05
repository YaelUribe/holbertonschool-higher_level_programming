#!/usr/bin/python3
"""
add_integer module:
function for addition of two integers
"""

def add_integer(a, b=98):
    """
    Function to add integers
    Parameters:
    ------------
    a : int or float
    b : int or float
    return
    ------------
    Returns an integer: the total of adding a and b
    """

    # Cast floats to integers to round their values
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    # Variables must be integers
    if not isinstance(a, int):
        raise TypeError("a must be an integer")
    elif not isinstance(b, int):
        raise TypeError("b must be an integer")

    # now we can return the given values as the product of an addition
    return a + b
