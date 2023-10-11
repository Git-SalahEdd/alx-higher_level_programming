#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """function that returns a set of all elements present in only one set."""
    diff_set = set()
    for element in set_1:
        if element not in set_2:
            diff_set.add(element)

    for element in set_2:
        if element not in set_1:
            diff_set.add(element)

    return diff_set
