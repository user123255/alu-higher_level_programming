#!/usr/bin/python3
"""
This module provides a function that adds two integers or floats
casted to integers.
"""


def add_integer(a=0, b=98):
    """
    Adds two integers or floats after casting them to integers.

    Args:
        a (int or float): first number (default 0)
        b (int or float, optional): second number (default 98)

    Raises:
        TypeError: If a or b is not an int or float.

    Returns:
        int: The addition of a and b cast to integers.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
