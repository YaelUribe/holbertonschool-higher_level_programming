#!/usr/bin/python3
"""
Module: Square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Square
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Square class constructor"""
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """String representation for a requested message"""
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id,
                                                         self.x,
                                                         self.y,
                                                         self.size)
