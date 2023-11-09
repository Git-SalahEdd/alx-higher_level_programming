#!/usr/bin/python3
""" Module for base Class"""


class Base:
    """This class will be the “base” of all other classes in this project."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Class Methode constructor
            args:
                self: self
                id: id"""

        if id is not None:
            self.id = id
        else:
            base.__nb_objects += 1
            self.id = base.__nb_objects
