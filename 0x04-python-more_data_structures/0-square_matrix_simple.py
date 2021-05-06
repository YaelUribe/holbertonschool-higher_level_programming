#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    copy = matrix.copy()
    return [list(map((lambda x: x * x), i)) for i in copy]
