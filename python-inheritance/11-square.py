#!/usr/bin/python3
"""
This module defines a Square class that inherits from Rectangle.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle.

    Attributes:
        __size (int): The size of the square's sides (private).
    """

    def __init__(self, size):
        """
        Initialize a Square.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size <= 0.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

    def __str__(self):
        """Return string representation of the square."""
        return f"[Square] {self.__size}/{self.__size}"
