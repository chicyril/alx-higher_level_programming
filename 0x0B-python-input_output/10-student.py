#!/usr/bin/python3
"""10-student Module."""


class Student:
    """Class that defines a Student."""
    def __init__(self, first_name, last_name, age):
        """Initialize instance attributes during instantiation."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return dictionary description of an instance."""
        if type(attrs) is list and all(isinstance(k, str) for k in attrs):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__.copy()
