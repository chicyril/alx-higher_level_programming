#!/usr/bin/python3
"""2-is_same_class Module."""


def is_same_class(obj, a_class):
    """Assert that an object is an instance of a class.

    Args:
        Obj: the object.
        a_class: the class to check.

    Return: True or False.
    """
    return type(obj) == a_class
