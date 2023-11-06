#!/usr/bin/python3
"""
Module for the class BaseGeometry
"""


class BaseGeometry:
    """
    Class with public instance methods: area and integer_validator
    """

    def area(self):
        """
        Raises Exception with msg 'area() is not implemented'
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Function that validates value

        Args:
            name (str)
            value (int)
        """
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
