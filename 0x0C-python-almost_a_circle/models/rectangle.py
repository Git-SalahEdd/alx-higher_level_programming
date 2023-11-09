#!/usr/bin/python3
"""
Module for the class Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle class inheriting from the Base class.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a Rectangle object.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate of the rectangle's position.
            y (int, optional): The y-coordinate of the rectangle's position.
            id (int, optional): The ID of the rectangle.
        """
        self.value_validator("id", id)
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Get the width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, width):
        """
        Set the width of the rectangle.
        """
        self.value_validator("width", width)
        self.__width = width

    @property
    def height(self):
        """
        Get the height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, height):
        """
        Set the height of the rectangle.
        """
        self.value_validator("height", height)
        self.__height = height

    @property
    def x(self):
        """
        Get the position x of the rectangle.
        """
        return self.__x

    @x.setter
    def x(self, x):
        """
        Set the position x of the rectangle.
        """
        self.value_validator("x", x)
        self.__x = x

    @property
    def y(self):
        """
        Get the position y of the rectangle.
        """
        return self.__y

    @y.setter
    def y(self, y):
        """
        Set the position y of the rectangle.
        """
        self.value_validator("y", y)
        self.__y = y
