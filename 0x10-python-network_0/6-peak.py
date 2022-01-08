#!/usr/bin/python3
"""Module: peak"""


def find_peak(list_of_integers):
    """Funcion to find a Peak in an unsorted list"""
    lenght = len(list_of_integers)
    if (lenght == 0):
        return None
    for i in range(lenght - 1):
        if (i == 0):
            i += 1
        elif (list_of_integers[i - 1] <= list_of_integers[i] and
              list_of_integers[i + 1] <= list_of_integers[i]):
            print("{}".format(list_of_integers[i]))
