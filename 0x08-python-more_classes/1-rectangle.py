#!/usr/bin/python3
"""Module for empty class Rectangle that defines a rectangle"""


class Rectangle:
    """empty class Rectangle that defines a rectangle."""
    def __init__(self, width=0, height=0):
        """"Initialize a new Rectangle.

            Args :
                width: distance between its two shorter sides or edges.
                height: longer sides of the rectangle
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """Properaty for width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise TypeError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Properaty for height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise TypeError("height must be >= 0")
        self.__height = value
