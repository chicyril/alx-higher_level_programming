#!/usr/bin/python3
"""8-rectangle Module."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle derive from BaseGeometry."""
    def __init__(self, width, height):
        """Initialize an instance attribute."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
