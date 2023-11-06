#!/usr/bin/python3
""" Module for Class MyInt that inherits  from int """


class MyInt(int):
    """ Class MyInt inherits from int """

    def __init__(self, value):
        """
        Initializing value
        """
        self.value = value

    def __eq__(self, other):
        """
        Returns invert of ==
        """
        return self.value != other

    def __ne__(self, other):
        """
        Returns invert of !=
        """
        return self.value == other
