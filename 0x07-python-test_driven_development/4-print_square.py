#!/usr/bin/python3
"""Module  that prints a square with the character #
"""


def print_square(size):
    """ function that prints a square with the character #.
        Args:
            ize: is the size length of the square
        Raise:
            TypeError: size must be an integer
            ValueError: size must be >= 0
            TypeError: size must be an integer not float and is >= 0

    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
