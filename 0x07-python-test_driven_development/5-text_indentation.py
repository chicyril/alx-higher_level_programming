#!/usr/bin/python3
"""5-text_indentation Module."""


def text_indentation(text):
    """Prints 2 new lines after any of '.', '?' or ':' in a text.

    Args:
        text(str): text input.
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    text_dup = text[:]

    for delim in ".?:":
        stripped_split = ([splitted.strip(' ')
                           for splitted in text_dup.split(delim)])
        text_dup = (delim + "\n\n").join(stripped_split)

    print(text_dup, end="")
