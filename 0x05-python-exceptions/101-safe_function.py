#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        total = fct(*args)
        return total
    except Exception as x:
        print("Exception: {}".format(x), file=sys.stderr)
        return None
