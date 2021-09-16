#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    copy = {}
    for i, j in a_dictionary.items():
        copy[i] = j * 2
    return copy
