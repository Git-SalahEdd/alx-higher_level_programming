#!/usr/bin/python3
"""
Module for the class Square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    class Square inheriting from Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a Square object.

        Args:
            size (int): The size of the square.
            x (int, optional): The x-coordinate of the square's position.
            y (int, optional): The y-coordinate of the square's position.
            id (int, optional): The ID of the square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Get the size of the square
        """
        return self.width

    @size.setter
    def size(self, size):
        """
        Set the size of the square
        """
        self.value_validator("width", size)
        self.width = size
        self.height = size
