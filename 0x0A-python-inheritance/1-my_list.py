#!/usr/bin/python3
"""
Module of the class MyList
"""


class MyList(list):
    """
    A class MyList that inherits from list
    """

    def print_sorted(self):
        """
        A function that prints the list, but sorted (ascending sort)

        Args:
            self
        """
        print(sorted(self))
