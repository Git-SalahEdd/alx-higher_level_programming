#!/usr/bin/python3
"""
Module for the class Rectangle
"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    Class Rectangle that inherits from BaseGeometry
    """

    def __init__(self, width, height):
        """
        Instantiation with width and height, private and positive ints

        Args:
            width (int)
            height (int)
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Returns area of rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns the following rectangle description:
        [Rectangle] <width>/<height>
        """
        return ("[" + type(self).__name__ + "] " + str(self.__width)
                + "/" + str(self.__height))
