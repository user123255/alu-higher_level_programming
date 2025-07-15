#!/usr/bin/python3
"""Defines the Student class with serialization and deserialization."""


class Student:
    """Defines a student with basic info and JSON methods."""

    def __init__(self, first_name, last_name, age):
        """Initialize student attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return dictionary representation of the instance.

        If `attrs` is a list of strings, only return specified attributes.
        Otherwise, return all public attributes.
        """
        if isinstance(attrs, list) and all(
            isinstance(attr, str) for attr in attrs
        ):
            return {
                attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)
            }
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the instance from a dictionary."""
        for key, value in json.items():
            setattr(self, key, value)
