#!/usr/bin/python3

def multiple_returns(sentence):
    """Return the length of a string and it's first characte"""

    return (len(sentence), sentence[0] if len(sentence) > 0 else None)
