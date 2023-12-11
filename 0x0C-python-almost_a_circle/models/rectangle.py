#!/usr/bin/python3
"""rectangle module: Defines a Rectangle class that is a subclass
of th Base class.
"""
from models.base import Base
import inspect


class Rectangle(Base):
    """Defines an object of <type Rectangle>."""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize instance attributes during instanciation."""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def __str__(self):
        return ("[Rectangle] ({}) {}/{} - {}/{}"
                .format(self.id, self.x, self.y, self.width, self.height))

    def area(self):
        """Compute the area of this triangle."""
        return self.width * self.height

    def display(self):
        """Print this rectangle with using the character '#'."""
        for i in range(self.y):
            print()
        for i in range(self.height):
            if self.x:
                print(' ' * self.x, end='')
            print('#' * self.width)

    def update(self, *args,  **kwargs):
        """Update the value of attributes."""
        attrList = ['id', 'width', 'height', 'x', 'y']
        for i, arg in enumerate(args):
            if i >= len(attrList):
                break
            attr = attrList[i]
            setattr(self, attr, arg)
        for key in kwargs.keys():
            if key in attrList and (attrList.index(key) >= len(args)):
                i = attrList.index(key)
                setattr(self, attrList[i], kwargs[key])

    def to_dictionary(self):
        """Returns a dictionary representation of a rectangle."""
        dicto = dict(inspect.getmembers(self, lambda attrs:
                                        not (inspect.isroutine(attrs))))
        return dict([kval for kval in dicto.items()
                     if not kval[0].startswith('_')])
