#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    nu_list = matrix.copy()
	return [list(map((lambda x: x * x), i)) for i in nu_list]
