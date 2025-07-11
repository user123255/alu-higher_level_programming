#!/usr/bin/python3
"""
This module defines a class named BaseGeometry
with a public method that raises an exception.
"""


class BaseGeometry:
    """
    A base geometry class with an unimplemented area method.
    """

    def area(self):
        """
        Raises an Exception indicating that area() is not implemented.
        """
        raise Exception("area() is not implemented")
