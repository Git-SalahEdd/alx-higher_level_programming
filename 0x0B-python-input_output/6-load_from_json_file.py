#!/usr/bin/python3
"""Module for the function load_from_json_file()"""


import json


def load_from_json_file(filename):
    """A function that creates an Object from a “JSON file”"""
    with open(filename, "r", encoding="utf-8") as file:
        return json.loads(file.read())
