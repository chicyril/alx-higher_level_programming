#!/usr/bin/python3
"""2-append_write Module."""


def append_write(filename="", text=""):
    """Apends text to a file."""
    with open(filename, 'a') as file:
        count = file.write(text)
    return count
