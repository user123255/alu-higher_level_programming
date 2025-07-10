#!/usr/bin/python3
"""Module for checking if an object is exactly an instance of a specified class."""

def is_same_class(obj, a_class):
    """Return True if the object is exactly an instance of the specified class; otherwise False.

    Args:
        obj: The object to check.
        a_class: The class to match against.

    Returns:
        bool: True if obj is an instance of a_class, otherwise False.
    """
    return type(obj) is a_class


# Example test cases
if __name__ == "__main__":
    a = 1
    print(is_same_class(a, int))          # True
    print(is_same_class(a, float))        # False
    print(is_same_class(a, object))       # True

    a = True
    print(is_same_class(a, int))          # False
    print(is_same_class(a, object))       # True

    a = 3.14
    print(is_same_class(a, int))          # False
    print(is_same_class(a, object))       # True

    a = None
    print(is_same_class(a, object))       # True
    print(is_same_class(a, list))         # False

    a = [1, 2, 3]
    print(is_same_class(a, list))         # True
    print(is_same_class(a, object))       # True
