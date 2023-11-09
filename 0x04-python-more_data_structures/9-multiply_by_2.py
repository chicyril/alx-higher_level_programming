#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    """Multiply the values of each key by 2 in another dictionary."""

    return ({key: val * 2 for key, val in a_dictionary.items()})
