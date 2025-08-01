#!/usr/bin/python3
from models.rectangle import Rectangle

class Square(Rectangle):
    """Square class that inherits from Rectangle"""

    def __init__(self, size, id=None):
        super().__init__(size, size, id)
