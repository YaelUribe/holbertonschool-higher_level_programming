#!/usr/bin/python3
"""
Module: class MyInt
"""


class MyInt(int):
	"""
	Class MyInt
	inherits from int
	"""
	def __init__(self, i):
		self.__i = i

	def __eq__(self, other):
		return int(self) != other

	def __ne__(self, other):
		return int(self) == other
