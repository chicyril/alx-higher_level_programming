#!/usr/bin/python3
"""8-class_to_json Module."""


def class_to_json(obj):
    """Retuns the dictionary description of an object."""
    d = {}
    if hasattr(obj, "__dict__"):
        d = obj.__dict__.copy()
    return d
