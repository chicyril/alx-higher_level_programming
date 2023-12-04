#!/usr/bin/python3
"""4-inherits_from Module."""


def inherits_from(obj, a_class):
    """Assert that an object is derived from a class.

    Args:
        Obj: the object.
        a_class: the class to check.

    Return: True or False.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
