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

    def value_validator(self, name, value):
        """
        Validate the value for a specific attribute.

        Args:
            name (str): The name of the attribute being validated.
            value: The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0 for
                    "width" or "height", or less than 0 for "x" or "y".
        """
        if value is not None and type(value) is not int:
            raise TypeError(name + " must be an integer")
        if (name == "width" or name == "height") and value <= 0:
            raise ValueError(name + " must be > 0")
        if (name == "y" or name == "x") and value < 0:
            raise ValueError(name + " must be >= 0")

    def area(self):
        """
        Calculate the area of the rectangle.
        """
        return self.width * self.height

    def display(self):
        """
        Display the rectangle by printing the "#" characters.
        """
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x, end="")
            for j in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """
        Return a string representation of the rectangle object.
        """
        s = "[{}] ({}) {}/{} - {}/{}".format(
            type(self).__name__, self.id, self.x,
            self.y, self.width, self.height
        )
        return s

    def update(self, *args, **kwargs):
        """
        Update the attributes of the rectangle object.

        Args:
            *args: Variable-length arguments representing attribute values.
            **kwargs: Keyword arguments representing attribute-value pairs.
        """
        if len(args) > 0:
            attrs = ["id", "width", "height", "x", "y"]
            i = 0
            for arg in args:
                setattr(self, attrs[i], arg)
                i += 1
        elif len(kwargs) > 0:
            for key in kwargs:
                setattr(self, key, kwargs[key])

    def to_dictionary(self):
        """
        Return a dictionary representation of the rectangle object.
        """
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y,
        }
