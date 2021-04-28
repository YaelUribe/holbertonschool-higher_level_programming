#!/usr/bin/python3
import sys
if __name__ == "__main__":
    total = 0
    argc = len(sys.argv)
    for x in range(1, argc):
        total += int(sys.argv[x])
    print("{}".format(total))
