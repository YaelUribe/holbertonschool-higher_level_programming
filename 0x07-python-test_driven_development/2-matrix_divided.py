#!/usr/bin/python3
"""
matrix_divided module:
Function to divide all elements of a matrix
"""

def matrix_divided(matrix, div):
	"""
	Function to divide elements of a matrix
	Parameters:
	-----------
	matrix : List of list (2 dimensional list)
			containing integers or floats
	div :	int or float to divide numbers by
	return
	-----------
	Returns a new matrix: The total of dividing each element of matrix
		by div
	"""
	# verify if matrix is a list of lists
	m_err = "matrix must be a matrix (list of lists) of integers/floats"
	if type(matrix) is not list:
		raise TypeError(m_err)
	for y in matrix:
		if type(y) is not list:
			raise TypeError(m_err)

	# verify "div" is not 0 and it is an integer
	if div == 0:
		raise ZeroDivisionError("division by zero")
	if type(div) is not int and type(div) is not float:
		raise TypeError("div must be a number")

	# Make sure every element in matrix is int or float
	for y in matrix:
		for x in y:
			if type(x) is not int and type(x) is not float:
				raise TypeError(m_err)

	# check all rows size
	l_rows = []
	for y in matrix:
		l_rows.append(len(y))
	l_rows = set(l_rows)
	if len(l_rows) > 1:
		raise TypeError("Each row of the matrix must have the same size")

	# In an empty list store the result of each division
	nu_matrix = []
	for rows in matrix:
		for column in rows:
			nu_matrix.append(round(column/div, 2))
	return nu_matrix
