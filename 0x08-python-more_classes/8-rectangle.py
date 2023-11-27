#!/usr/bin/python3
"""8-rectangle Module."""


class Rectangle:
    """Rectangle class type."""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Ininialize attributes during instantiation.

        Args:
            width(int): width of the rectangle.
            height(int): height of the rectangle.
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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

    def area(self):
        """Computes the area of the rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Computes the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return (2 * (self.__width + self.__height))

    def __str__(self):
        """Return a recangular shape made of '#'."""
        if self.__width is 0 or self.__height is 0:
            return ("")
        return ("\n".join(["".join([str(self.print_symbol)
                                    for i in range(self.__width)])
                           for j in range(self.__height)]))

    def __repr__(self):
        """Return a string representation of the the instance"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Delete an instatnce."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2
