#!/usr/bin/python3
"""
A module for the function is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """
    A function that returns True if the object is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class ; otherwise False.

    Args:
        obj: object to be checked
        a_class: class to be checked in
    """
    return isinstance(obj, a_class)
