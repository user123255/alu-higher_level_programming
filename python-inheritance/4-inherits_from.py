#!/usr/bin/python3
"""Module for checking if an object is an instance of a subclass of a specified class."""

def inherits_from(obj, a_class):
    """Return True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class; otherwise False.

    Args:
        obj: The object to check.
        a_class: The class to match against.

    Returns:
        bool: True if obj is an instance of a subclass of a_class, otherwise False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class


# Example test cases
if __name__ == "__main__":
    a = True
    if inherits_from(a, int):
        print("{} inherited from class {}".format(a, int.__name__))
    if inherits_from(a, bool):
        print("{} inherited from class {}".format(a, bool.__name__))
    if inherits_from(a, object):
        print("{} inherited from class {}".format(a, object.__name__))
