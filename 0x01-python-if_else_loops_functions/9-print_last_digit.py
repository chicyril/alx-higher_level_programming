#!/usr/bin/python3
def print_last_digit(number):
    """Print and return the last digit of a number"""

    ld = abs(number) % 10
    print(ld, end="")
    return (ld)
