#!/usr/bin/python3

def safe_function(fct, *args):
    import sys
    try:
        result = fct(*args)
    except Exception as errmsg:
        sys.stderr.write("Exception: {}\n".format(errmsg))
        result = None
    return (result)
