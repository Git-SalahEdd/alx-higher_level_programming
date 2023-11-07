#!/usr/bin/python3
"""
Module for the function ()
"""


def append_write(filename="", text=""):
    """
    a function that appends a string
    at the end of a text file (UTF8)
    and returns the number of characters added

    Args:
        filename (str): name of file
        text (str): content to be appended
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
