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

    def __str__(self):
        """
        Return a string representation of the square object.
        """
        s = "[{}] ({}) {}/{} - {}".format(
            type(self).__name__, self.id, self.x, self.y, self.width
        )
        return s

    def update(self, *args, **kwargs):
        """
        Update the attributes of the square object.

        Args:
            *args: Variable-length arguments representing attribute values.
            **kwargs: Keyword arguments representing attribute-value pairs.
        """
        if len(args) > 0:
            attrs = ["id", "size", "x", "y"]
            i = 0
            for arg in args:
                setattr(self, attrs[i], arg)
                i += 1
            return
        for key in kwargs:
            setattr(self, key, kwargs[key])

    def to_dictionary(self):
        """
        Return a dictionary representation of the square object.
        """
        return {"id": self.id, "size": self.width, "x": self.x, "y": self.y}
