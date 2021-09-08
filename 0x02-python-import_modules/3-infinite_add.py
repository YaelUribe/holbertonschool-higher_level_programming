#!/usr/bin/python3
import sys
if __name__ == "__main__":
    result = 0
    argc = len(sys.argv)
    for x in range(1, argc):
        result += int(sys.argv[x])
    print("{}".format(result))
