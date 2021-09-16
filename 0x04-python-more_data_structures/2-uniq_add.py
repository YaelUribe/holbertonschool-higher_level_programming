#!/usr/bin/python3
def uniq_add(my_list):
    uniq= []
    for x in my_list:
        if x not in uniq:
            uniq.append(x)
    y= 0
    for i in uniq:
        y += i
    return y
