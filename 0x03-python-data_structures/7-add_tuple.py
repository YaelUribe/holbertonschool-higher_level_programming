#!/usr/bin/python3
def add_tuple(tuple_a, tuple_b):
	i = len(tuple_a)
	b = len(tuple_b)
	if i > 0 and b > 0:
		tuple_total[0]= (tuple_a[0] + tuple_b[0])

	if i > 1 and b > 1:
		tuple_total[1] = (tuple_a[1] + tuple_b[1])

		return tuple_total
