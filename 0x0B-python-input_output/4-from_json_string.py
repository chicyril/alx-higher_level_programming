#!/usr/bin/python3
"""4-from_json_string Module."""
import json


def from_json_string(my_str):
    """Return a python data structure from a json string."""
    return json.loads(my_str)
