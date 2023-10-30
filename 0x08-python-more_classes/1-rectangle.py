#!/usr/bin/python3
"""
Module to create a class Rectangle
"""


class Rectangle:
    """
    Class named Rectangle
    """

    def __init__(self, width=0, height=0):
        """
        Class initializer

        Args:
            self : Argument
            width : Argument
                (default is 0)
            height : Argument
                (default is 0)

        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """
        Width getter

        Args:
            self : Argument

        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Width setter

        Args:
            self : Argument
            value : Argument

        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Height getter

        Args:
            self : Argument

        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Height setter

        Args:
            self : Argument
            value : Argument

        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
