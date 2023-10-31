#!/usr/bin/python3
"""
Module for class LockedClass
"""


class LockedClass:
    """
    class LockedClass
    Prevents any attrs other than first_name
    """
    __slots__ = ["first_name"]
