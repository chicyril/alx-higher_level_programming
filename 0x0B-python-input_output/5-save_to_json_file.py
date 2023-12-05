#!/usr/bin/python3
"""5-save_to_json_file Module."""
import json


def save_to_json_file(my_obj, filename):
    """Write json of an object to a file."""
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
