#!/usr/bin/python3
def remove_char_at(str, n):
    str1 = ""
    for a in range(0, len(str)):
        if a == n:
            continue
        str1 = str1 + str[a]
    return str1
