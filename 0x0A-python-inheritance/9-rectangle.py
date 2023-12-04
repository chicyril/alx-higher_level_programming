#!/usr/bin/python3
"""9-rectangle Module."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle derive from BaseGeometry."""
    def __init__(self, width, height):
        """Initialize an instance attribute."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Compute the area of a rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """String representation of the instance."""
        return f"[Rectangle] {str(self.__width)}/{str(self.__height)}"
