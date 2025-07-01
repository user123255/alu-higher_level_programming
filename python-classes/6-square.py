#!/usr/bin/python3
"""Defines a class Square with position and print capability."""


class Square:
    """Represents a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square with size and position.

        Args:
            size (int): The size of the square.
            position (tuple): Tuple of 2 positive integers representing position.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size with validation.

        Args:
            value (int): Size to set.
        Raises:
            TypeError: If not an integer.
            ValueError: If less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position with validation.

        Args:
            value (tuple): Tuple of 2 positive integers.
        Raises:
            TypeError: If not a valid tuple.
        """
        if (
            not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(num, int) for num in value) or
            not all(num >= 0 for num in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square using '#' with position offset."""
        if self.__size == 0:
            print()
            return

        # Print vertical space (position[1])
        for _ in range(self.__position[1]):
            print()

        # Print each row with horizontal space (position[0])
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

