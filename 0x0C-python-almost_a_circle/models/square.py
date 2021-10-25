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

    @property
    def size(self):
        """Size getters"""
        return self.width

    @size.setter
    def size(self, value):
        """Size setters"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Public method to assign an argument to each attribute
        args: kind of a single pointer to a dictionary
        kwargs: dictionary with key/value args
        """
        if args and len(args) > 0:
            for index, arg in enumerate(args):
                if index == 0:
                    self.id = arg
                if index == 1:
                    self.size = arg
                if index == 2:
                    self.x = arg
                if index == 3:
                    self.y = arg
        elif kwargs and len(kwargs) > 0:
            for k, v in kwargs.items():
                if k == 'id':
                    self.id = v
                if k == 'size':
                    self.size = v
                if k == 'x':
                    self.x = v
                if k == 'y':
                    self.y = v

    def to_dictionary(self):
        """
        Returns Dictionary repr of Square
        """
        attributes = ['id', 'size', 'x', 'y']
        return {key: getattr(self, key) for key in attributes}
