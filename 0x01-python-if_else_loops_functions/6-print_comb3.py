#!/usr/bin/python3
for x in range(48, 57):
    for y in range(48, 58):
        if x == y or x > y:
            continue
        if x == 56 and y == 57:
            continue
        print("{}{}".format(chr(x), chr(y)), end=", ")
print("{}{}".format(chr(x), chr(y)))
