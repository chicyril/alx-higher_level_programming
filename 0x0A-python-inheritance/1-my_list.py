#!/usr/bin/python3
"""1-my_list Module."""


class MyList(list):
    """A sub-class of python list.

    Arg:
        list(class): the python list class.
    """
    def print_sorted(self):
        """Print out the elements in the list in sorted order."""
        print(sorted(self))
