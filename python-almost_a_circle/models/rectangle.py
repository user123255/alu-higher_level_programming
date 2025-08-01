#!/usr/bin/python3
from models.base import Base

class Rectangle(Base):
    """Rectangle class that inherits from Base"""

    def __init__(self, width, height, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
