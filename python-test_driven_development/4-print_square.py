#!/usr/bin/python3
"""
This module defines a function that prints a square with '#'
"""

def print_square(size):
    """
    Prints a square with '#' characters.

    Args:
        size (int): size of the square (length and height)

    Raises:
        TypeError: if size is not an integer or is a float
        ValueError: if size is less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
