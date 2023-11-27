#!/usr/bin/python3
"""1-rectangle Module."""


class Rectangle:
    """Rectangle class type."""

    def __init__(self, width=0, height=0):
        """Ininialize attributes during instantiation.

        Args:
            width(int): width of the rectangle.
            height(int): height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the value of the width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the value of the width attribute.

        Args:
            value(int): width.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the value of the height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the value of the height attribute.

        Args:
            value(int): heght.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
