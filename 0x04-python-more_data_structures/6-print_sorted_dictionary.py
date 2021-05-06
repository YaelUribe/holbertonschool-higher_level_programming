#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    copy = a_dictionary.copy()
    for x, y in sorted(copy.items()):
        print("{}: {}".format(x, y))
