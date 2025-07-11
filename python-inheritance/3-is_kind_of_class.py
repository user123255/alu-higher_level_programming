#!/usr/bin/python3
"""
This module defines a function that checks
if an object is an instance of a specified class or its subclasses.
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance of the specified class
    or a class that inherited from it.
    Otherwise, returns False.

    Args:
        obj: The object to check
        a_class: The class to compare against

    Returns:
        True if obj is an instance or inherits from a_class, False otherwise.
    """
    return isinstance(obj, a_class)
