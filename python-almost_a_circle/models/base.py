#!/usr/bin/python3
"""Base class module"""

import json

class Base:
    """Base class for managing id attribute in all future classes"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Return the list of dictionaries from a JSON string"""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)
