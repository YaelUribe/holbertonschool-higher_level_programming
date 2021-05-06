#!/usr/bin/python3
def search_replace(my_list, search, replace):
    copy = []
    for x in my_list:
        if x is search:
            copy.append(replace)
        else:
            copy.append(x)
    return copy
