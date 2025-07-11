#!/usr/bin/python3
"""
This module defines a Rectangle class that inherits from BaseGeometry.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class inherits from BaseGeometry.

    Attributes:
        __width (int): Width of the rectangle (private).
        __height (int): Height of the rectangle (private).
    """

    def __init__(self, width, height):
        """
        Initialize Rectangle with width and height.

        Args:
            width (int): Positive integer width.
            height (int): Positive integer height.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height <= 0.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return string representation: [Rectangle] <width>/<height>"""
        return f"[Rectangle] {self.__width}/{self.__height}"
