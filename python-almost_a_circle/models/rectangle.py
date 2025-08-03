#!/usr/bin/python3
"""Defines the Rectangle class."""

from models.base import Base


class Rectangle(Base):
    """Rectangle class that inherits from Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.validate_integer("width", value)
        self.validate_greater_than_zero("width", value)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.validate_integer("height", value)
        self.validate_greater_than_zero("height", value)
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.validate_integer("x", value)
        self.validate_non_negative("x", value)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.validate_integer("y", value)
        self.validate_non_negative("y", value)
        self.__y = value

    def validate_integer(self, name, value):
        """Validate that value is an integer.

        Args:
            name (str): The name of the attribute.
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

    def validate_greater_than_zero(self, name, value):
        """Validate that value is greater than zero.

        Args:
            name (str): The name of the attribute.
            value (int): The value to validate.

        Raises:
            ValueError: If value is less than or equal to zero.
        """
        if value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def validate_non_negative(self, name, value):
        """Validate that value is zero or positive.

        Args:
            name (str): The name of the attribute.
            value (int): The value to validate.

        Raises:
            ValueError: If value is negative.
        """
        if value < 0:
            raise ValueError("{} must be >= 0".format(name))

