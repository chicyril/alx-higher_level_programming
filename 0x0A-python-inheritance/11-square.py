#!/usr/bin/python3
"""11-square Module."""
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

    def __str__(self):
        """Return string representation of instance."""
        return f"[Square] {str(self.__size)}/{str(self.__size)}"
