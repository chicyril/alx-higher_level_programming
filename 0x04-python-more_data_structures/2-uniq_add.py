#!/usr/bin/python3

def uniq_add(my_list=[]):
    """Sum up first occurrence of each element in a list."""

    return (sum(x for x in set(my_list)))
