#!/usr/bin/python3
def remove_char_at(str, n):
    str2 = ""
    for a in range(0, len(str)):
        if a == n:
            continue
        str2 = str2 + str[a]
    return str2
