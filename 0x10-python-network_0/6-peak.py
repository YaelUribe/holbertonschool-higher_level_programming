#!/usr/bin/python3
"""Module: peak"""

from typing import List


def find_peak(list_of_integers):
    """Funcion to find a Peak in an unsorted list"""
    lenght = len(list_of_integers)
    peak_s = ""
    if (len <= 1):
        return None
    for i in range(lenght - 1):
        if (list_of_integers[i - 1] == NULL):
            i += 1
        if (list_of_integers[i] == list_of_integers[lenght]):
            
        