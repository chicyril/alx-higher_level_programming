#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """Print the items in a dictionary by sorted keys."""

    [print("{}: {}".format(key, val))
        for key, val in sorted(a_dictionary.items())]
