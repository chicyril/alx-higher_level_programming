#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """Replace an element in a list in a new list."""

    return ([el if el != search else replace for el in my_list])
