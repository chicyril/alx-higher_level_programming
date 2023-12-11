#!/usr/bin/python3
"""Square module: defines a class square."""
from models.rectangle import Rectangle
import inspect


class Square(Rectangle):
    """Rectangle class definition."""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize attributes during instanciation."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """Return the string representation of a Square instance."""
        return ("[Square] ({}) {}/{} - {}"
                .format(self.id, self.x, self.y, self.width))

    def update(self, *args, **kwargs):
        """Update the values of attributes of a square instance."""
        attrList = ['id', 'size', 'x', 'y']
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
        """Return a dictionary representation of a Square instance."""
        dicto = dict(inspect.getmembers(self, lambda attrs:
                                        not (inspect.isroutine(attrs))))
        return dict([kval for kval in dicto.items()
                     if not kval[0].startswith('_')
                     if not kval[0] in ['height', 'width']])
