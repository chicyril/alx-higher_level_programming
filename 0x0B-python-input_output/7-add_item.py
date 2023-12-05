#!/usr/bin/python3
"""7-add_item Module."""

if __name__ == '__main__':
    import json
    import sys

    load_from_json_file =\
        __import__('6-load_from_json_file').load_from_json_file
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

    jfile = 'add_item.json'
    try:
        list_obj = load_from_json_file(jfile)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        list_obj = []
    if type(list_obj) is not list:
        list_obj = []
    list_obj.extend(sys.argv[1:])
    save_to_json_file(list_obj, jfile)
