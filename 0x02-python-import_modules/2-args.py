#!/usr/bin/python3
import sys
if __name__ == "__main__":
    args = len(sys.argv)
    if args == 1:
        print("{} arguments.".format(args - 1))
    elif args == 2:
        print("{} argument:".format(args - 1))
    elif args > 2:
        print("{} arguments:".format(args - 1))
