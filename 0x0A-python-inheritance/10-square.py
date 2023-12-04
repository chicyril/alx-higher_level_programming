#!/usr/bin/python3
"""10-square Module."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class derived from Rectangle."""
    def __init__(self, size):
        """Initialize an instance attribute."""
        self.integer_validator('size', size)
        self.__size = size

    def area(self):
        """Compute the area of a rectangle."""
        return self.__size * self.__size
