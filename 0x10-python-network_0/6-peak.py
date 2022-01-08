#!/usr/bin/python3
"""Module: peak"""


def find_peak(list_of_integers):
    """Funcion to find a Peak in an unsorted list"""
    lenght = len(list_of_integers)
    if (lenght == 0):
        return None
    list_of_integers.sort()
    return list_of_integers[-1]
