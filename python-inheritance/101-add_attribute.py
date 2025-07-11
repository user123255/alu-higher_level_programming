#!/usr/bin/python3
"""Defines a function that adds an attribute to an object if possible."""


def add_attribute(obj, name, value):
    """Adds a new attribute to an object if it's possible.

    Args:
        obj: The object to add the attribute to.
        name (str): The name of the attribute.
        value: The value to assign to the attribute.

    Raises:
        TypeError: If the object cannot accept new attributes.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
