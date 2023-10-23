#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """prints x elements of a list."""
    i = 0
    try:
        while i is not x:
            print(my_list[i], end='')
            i += 1
    except IndexError:
        None
    print()
    return i
