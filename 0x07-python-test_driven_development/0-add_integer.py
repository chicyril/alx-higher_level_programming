#!/usr/bin/python3
"""0-add_integer module."""


def add_integer(a, b=98):
    """Compute the sum of two ints a and b.

    Args:
        a (int): the first operand.
        b (int): the second operand.

    Return:
        int: the sum.
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")

    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
