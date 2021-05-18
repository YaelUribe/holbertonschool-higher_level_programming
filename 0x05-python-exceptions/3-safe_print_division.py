#!/usr/bin/python3
def safe_print_division(a, b):
    total = 0
    try:
        total = a / b
    except ZeroDivisionError:
        total = None
        return None
    finally:
        print("Inside reult: {}".format(total))
    return total
