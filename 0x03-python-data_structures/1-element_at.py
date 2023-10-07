#!/usr/bin/python3
def element_at(my_list, idx):
    """Function that retrieves an element from a list like in C."""
    if idx < 0 or idx >= len(my_list):
        return None

    for i in range(len(my_list)):
        if i == idx:
            return my_list[i]
