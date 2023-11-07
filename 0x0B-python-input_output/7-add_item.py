#!/usr/bin/python3
"""
Module to adds all arguments to a Python list,
and then save them to a file
"""
from sys import argv

load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file

try:
    exist = load_from_json_file("add_item.json")
except FileNotFoundError:
    exist = []
exist.extend(argv[1:])
save_to_json_file(exist, "add_item.json")
