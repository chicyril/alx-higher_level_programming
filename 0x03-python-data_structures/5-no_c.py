#!/usr/bin/python3

def no_c(my_string):
    """Remove all occurence of c in a copy of a string."""

    new = "".join([char for char in my_string if char.lower() != 'c'])
    return (new)
