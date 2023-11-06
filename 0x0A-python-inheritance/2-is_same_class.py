#!/usr/bin/python3
"""
A module of the function is_same_class
"""


def is_same_class(obj, a_class):
    """
    A function that returns True if the object is exactly
    an instance of the specified class ; otherwise False.

    Args:
        obj: object to be checked
        a_class: class to be checked in
    """
    return type(obj) == a_class
