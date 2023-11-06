#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """Add the elements of 2 tuples to form a resulting tuple."""

    tuple_a += (0, 0)
    tuple_b += (0, 0)
    tuple_a = tuple_a[:2]
    tuple_b = tuple_b[:2]
    tuple_c = tuple([x + y for x, y in zip(tuple_a, tuple_b)])
    return (tuple_c)
