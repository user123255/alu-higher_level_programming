#!/usr/bin/python3
"""
This module defines a class named BaseGeometry
with methods for area calculation and integer validation.
"""


class BaseGeometry:
    """
    A base geometry class with an unimplemented area method
    and an integer validator.
    """

    def area(self):
        """
        Raises an Exception indicating that area() is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that value is a positive integer.

        Args:
            name (str): The name of the parameter.
            value (any): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
