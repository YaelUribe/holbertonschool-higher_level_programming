#!/usr/bin/python3
def no_c(my_string):
    nu_string = ""
    for x in my_string:
        if x != 'C' and x != 'c':
            nu_string += x
    return nu_string
