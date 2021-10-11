#!/usr/bin/python3
"""
method: class MyInt
"""


class MyInt(int):
	"""
	Class MyInt
	inherits from int
	"""
	def __init__(self, i):
		self.__i = i

	def __eq(self, other):
		return self.__i == other.i

	def __ne__(self, other):
		return not self == other
