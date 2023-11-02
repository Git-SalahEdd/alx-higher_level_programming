#!/usr/bin/python3
"""
    Module for  prints My name is <first name> <last name> 3-say_my_name
"""


def say_my_name(first_name, last_name=""):
    """function that prints My name is <first name> <last name>
        Args:
            first_name: first parameter for first name
            last_name:  seconde parameter for last name
        Raises:
            TypeError:  first_name must be a string or
            last_name must be a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
