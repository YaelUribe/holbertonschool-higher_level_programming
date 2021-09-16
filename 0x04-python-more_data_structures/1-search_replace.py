#!/usr/bin/python3
def search_replace(my_list, search, replace):
    nu_list = []
    for i in my_list:
        if i is search:
            nu_list.append(replace)
        else:
            nu_list.append(i)
    return nu_list
