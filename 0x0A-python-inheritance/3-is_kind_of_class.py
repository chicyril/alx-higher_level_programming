#!/usr/bin/python3
"""3-is_kind_of_class Module."""


def is_kind_of_class(obj, a_class):
    """Assert that an object is an instance of a class.

    Args:
        Obj: the object.
        a_class: the class to check.

    Return: True or False.
    """
    return isinstance(obj, a_class)
