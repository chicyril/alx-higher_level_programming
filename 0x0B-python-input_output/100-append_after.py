#!/usr/bin/python3
"""100-append_after Module."""


def append_after(filename="", search_string="", new_string=""):
    """Insert a line with new_string after any line containing search_string."""
    with open(filename, 'r', encoding='utf-8') as file:
        append = False
        new_text = ""
        for line in file:
            new_text += line
            if search_string in line:
                new_text += new_string
                if not append:
                    append = True
    if append:
        with open(filename, 'w', encoding='utf-8') as writefile:
            writefile.write(new_text)
