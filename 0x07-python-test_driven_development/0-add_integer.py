#!/usr/bin/python3
"""Module for add_integer method.
"""


def add_integer(a, b=98):
    """ Adds two integers a and b

    Args:
        a : the first integer
        b : the second integer default value is 98
    Raises:
        TypeError : if a or b are not integers
    Return:
        sum of the two integers a and b"""

    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
