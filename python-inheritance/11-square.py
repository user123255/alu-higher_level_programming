#!/usr/bin/python3
"""Module that defines a Square class inheriting from Rectangle."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square using width and height from Rectangle."""

    def __init__(self, size):
        """
        Initializes a Square with a given size.

        Args:
            size (int): The size of the square's sides (must be > 0).
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Returns a string representation of the square."""
        return f"[Square] {self.__size}/{self.__size}"

    def area(self):
        """Calculates the area of the square."""
        return self.__size ** 2
