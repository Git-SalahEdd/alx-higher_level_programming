#!/usr/bin/python3
"""
Module of the class Student
"""


class Student:
    """
    class Student that defines a student
    """

    def __init__(self, first_name, last_name, age):
        """
        Instantiation of the class Student

        Args:
            first_name (str)
            last_name (str)
            age (int)
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieves a dictionary representation of a Student instance
        """
        return self.__dict__
