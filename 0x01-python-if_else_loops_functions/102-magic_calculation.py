#!/usr/bin/python3
def magic_calculation(a, b, c):
    """Does exactly as the provided python bytecode."""

    if a < b:
        return (c)
    if c > b:
        return (a + b)
    return (a*b - c)
