#!/usr/bin/python3

def max_integer(my_list=[]):
    """Find the int of the highest value in a list of ints."""

    if not my_list:
        return (None)
    maxx = my_list[0]
    for el in my_list:
        if el > maxx:
            maxx = el
    return (maxx)
