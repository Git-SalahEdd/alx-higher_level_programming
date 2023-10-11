#!/usr/bin/python3
def uniq_add(my_list=[]):
    """function that adds
    all unique integers in a list (only once for each integer)."""
    new_list = []
    unique_set = set()
    for item in my_list:
        if item not in unique_set:
            new_list.append(item)
            unique_set.add(item)
    result = 0
    for i in range(len(new_list)):
         result += new_list[i]
    return result
