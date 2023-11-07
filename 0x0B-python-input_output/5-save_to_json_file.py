#!/usr/bin/python3
"""Module for the function save_to_json_file"""


import json


def save_to_json_file(my_obj, filename):
    """A function that writes an Object to a text file using a JSON representation
        Args:
        my_obj (obj): content to be JSON-ed and written
        filename (str): name of file"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
