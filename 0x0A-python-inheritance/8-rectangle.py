#!/usr/bin/python3
"""
Module - class BaseGeometry
"""


class BaseGeometry():
    """class BaseGeometry"""
    def area(self):
        """
        function to define an area
        meanwhile raises an Exception
        """
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """
        function to validate a given value
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
	"""class Rectangle that inheritates from
		BaseGeometry class
	"""
	def __init__(self, width, height):
		self.__width = width
		self.__height = height

		BaseGeometry.__init__(self)
