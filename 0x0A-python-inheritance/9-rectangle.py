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
		"""instantiation for Rectangle"""
		self.integer_validator("width", width)
		self.__width = width
		self.integer_validator("height", height)
		self.__height = height

	def area(self):
		"""re defining the area function"""
		return self.__width * self.__height

	def __str__(self):
		"""print the message requested"""
		print("[Rectangle] {:d}/{:d}".format(self.__width, self.__height))
