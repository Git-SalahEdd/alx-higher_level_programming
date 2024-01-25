#!/usr/bin/python3
"""
Module for find_peak function
"""


def find_peak(list_of_integers):
    """
    Function that finds a peak in a list of unsorted integers
    using a binary search algorithm
    """
    left, right = 0, len(list_of_integers) - 1

    if not list_of_integers:
        return None
    while left < right:
        mid = left + (right - left) // 2

        if list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return list_of_integers[left]
