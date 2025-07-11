#!/usr/bin/python3
"""Defines a class MyInt that inherits from int and inverts equality operators."""


class MyInt(int):
    """A rebel integer that inverts == and != operators."""

    def __eq__(self, other):
        """Invert == to behave like !="""
        return super().__ne__(other)

    def __ne__(self, other):
        """Invert != to behave like =="""
        return super().__eq__(other)
