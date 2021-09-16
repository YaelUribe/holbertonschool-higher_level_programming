#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
     copy = a_dictionary.copy()
    copy[key] = value
    return copy
