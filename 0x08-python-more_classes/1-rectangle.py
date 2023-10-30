#!/usr/bin/python3
"""Module for empty class Rectangle that defines a rectangle"""


class Rectangle:
    """empty class Rectangle that defines a rectangle."""
    def __init__(self, width=0, height=0):
        """Class method

            Args :
                width: distance between its two shorter sides or edges.
                height: longer sides of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Properaty for width of the rectangle
            Raises:
                TypeError: width must be an integer
                ValueError: width must be >= 0
        """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if not value >= 0:
            raise TypeError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Properaty for height of the rectangle
            Raises:
                TypeError: height must be an integer
                ValueError: height must be >= 0
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if not value >= 0:
            raise TypeError("height must be >= 0")
        self.__height = value
