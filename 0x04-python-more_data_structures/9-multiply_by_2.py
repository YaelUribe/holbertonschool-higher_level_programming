#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    copy = {}
    for x, y in a_dictionary.items():
        copy[x] = y * 2
    return copy
