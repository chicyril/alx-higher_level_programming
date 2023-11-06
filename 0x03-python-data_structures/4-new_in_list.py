#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """Replace an element at index idx in a shallow copy of a list"""

    cpy = my_list.copy()
    if 0 <= idx < len(cpy):
        cpy[idx] = element
    return (cpy)
