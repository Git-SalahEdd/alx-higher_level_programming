#!/usr/bin/python3
""" Square Module """


class Square:
    """ Define Square """
    def __init__(self, size=0):
        """Constroctor.

        Args :
            size : lenth of a side of the Square.
        """
        self.size = size

    @property
    def size(self):
        """properaty for the square

        Raises:
            TypeError: size must be an integer
            ValueError: size must be >= 0
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if not value >= 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Constroctor.
            returns the current square area
        """
        return self.__size ** 2
