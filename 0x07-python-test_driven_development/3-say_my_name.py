#!/usr/bin/python3
"""
say_my_name module:
Function to rpint My name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """
    Function to print My name is
    Parameters:
    -----------
    first_name :
    last_name:
    print
    -----------
    Prints My name is <first name> <last name>
    """
    # check that first_name and last_name are strings
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    elif type(last_name) is not str:
        raise TypeError("last_name must be a string")

    # print the values as a string
    print("My name is {} {}".format(first_name, last_name))
