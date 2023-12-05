#!/usr/bin/python3
"""1-write_file Module."""


def write_file(filename="", text=""):
    """Wrint string to text file."""
    with open(filename, 'w') as file:
        writeCount = file.write(text)
    return writeCount
