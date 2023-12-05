#!/usr/bin/python3
"""9-student Module."""


class Student:
    """Class student."""

    def __init__(self, first_name, last_name, age):
        """Initialize instance attributes during instantiation."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return dictionary description of an instance."""
        return self.__dict__.copy()
