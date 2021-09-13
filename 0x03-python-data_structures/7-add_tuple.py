#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    i = len(tuple_a)
    b = len(tuple_b)
    tuple_add = ((tuple_a[0] if i > 0 else 0) + (tuple_b[0] if b > 0 else 0),
                 (tuple_a[1] if i > 1 else 0) + (tuple_b[1] if b > 1 else 0))
    return tuple_add
