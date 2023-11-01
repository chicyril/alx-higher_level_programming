#!/usr/bin/python3
def uppercase(str):
    """Converts a string to uppercase characters"""

    outstr = ""
    for c in str:
        if 97 <= ord(c) <= 122:
            c = chr(ord(c) - 32)
        outstr += c
    print("{}".format(outstr))
