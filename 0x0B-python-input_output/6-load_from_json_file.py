#!/usr/bin/python3
"""6-load_from_json_file Module."""
import json


def load_from_json_file(filename):
    """Return a python object from a json file."""
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
