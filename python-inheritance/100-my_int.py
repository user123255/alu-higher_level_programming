#!/usr/bin/python3
"""Defines a class MyInt that inherits from int.

This class inverts the == and != operators.
"""


class MyInt(int):
    """A rebel integer that inverts == and !=."""

    def __eq__(self, other):
        """Invert == to behave like !="""
        return super().__ne__(other)

    def __ne__(self, other):
        """Invert != to behave like =="""
        return super().__eq__(other)
