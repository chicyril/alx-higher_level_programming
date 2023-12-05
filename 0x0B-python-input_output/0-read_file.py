#!/usr/bin/python3
"""0-read_file Module."""


def read_file(filename=""):
    """Reads text contents in a file."""
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end="")
