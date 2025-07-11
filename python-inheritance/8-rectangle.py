#!/usr/bin/python3
"""
This module defines a Rectangle
class that inherits from BaseGeometry.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class inherits from BaseGeometry.

    Instantiation with width and height:
        - width and height are private attributes
        - validated to be positive integers
        using integer_validator
        - no getters or setters for width or height
    """

    def __init__(self, width, height):
        """
        Initialize a Rectangle instance.

        Args:
            width (int): The width of the rectangle;
              must be a positive integer.
            height (int): The height of the rectangle;
              must be a positive integer.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is <= 0.
            TypeError: If arguments are missing.
        """
        # Validate parameters using BaseGeometry's method
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        # Set private attributes
        self.__width = width
        self.__height = height
