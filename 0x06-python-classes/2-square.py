#!/usr/bin/python3
""" Square Module """


class Square:
    """ Define Square """
    def __init__(self, size=0):
        """Constroctor.

        Args :
            size : lenth of a side of the Square.

        Raises:
            TypeError: size must be an integer
            ValueError: size must be >= 0
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if not size >= 0:
            raise ValueError('size must be >= 0')
        self.__size = size
