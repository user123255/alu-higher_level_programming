#!/usr/bin/python3
from models.base import Base

class Rectangle(Base):
    """Rectangle class that inherits from Base"""

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
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return area of the rectangle"""
        return self.width * self.height

    def display(self):
        """Print the rectangle using `#` considering x and y offsets"""
        print("\n" * self.y, end="")
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Return string representation"""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """Update attributes: id, width, height, x, y"""
        attrs = ['id', 'width', 'height', 'x', 'y']
        if args:
            for i, val in enumerate(args):
                if i < len(attrs):
                    setattr(self, attrs[i], val)
        else:
            for k, v in kwargs.items():
                if k in attrs:
                    setattr(self, k, v)

    def to_dictionary(self):
        """Return dictionary representation"""
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }

    @classmethod
    def create(cls, **dictionary):
        """Create instance with attributes set"""
        dummy = cls(1, 1)  # create dummy instance
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def save_to_file(cls, list_objs):
        """Write JSON string representation of list_objs to a file"""
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                f.write(Base.to_json_string(list_dicts))

    @classmethod
    def load_from_file(cls):
        """Load list of instances from a JSON file"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as f:
                list_dicts = Base.from_json_string(f.read())
                return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return []
