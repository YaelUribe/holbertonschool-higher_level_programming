#!/usr/bin/python3
"""Function to prevent dinamic creation of
    new instance attributes"""


class LockedClass:
    """Created Class"""
    __slots__ = ["first_name"]
