#!/usr/bin/python3
"""Function that returns the dictionary description for JSON serialization of an object."""

def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    (list, dictionary, string, integer, and boolean) for JSON serialization of an object.

    Args:
        obj: instance of a class

    Returns:
        dict: dictionary containing all attributes of obj
    """
    return obj.__dict__
