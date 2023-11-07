#!/usr/bin/python3
"""
Module for the function pascal_triangle()
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing
    the Pascal’s triangle of n

    Args:
        n (int)
    """
    if n <= 0:
        return []
    tri = [[1]]
    for i in range(n - 1):
        smol_tri = []
        for j in range(i + 2):
            if j == 0:
                x = 0
                y = tri[i][j]
            elif j == i + 1:
                x = tri[i][j - 1]
                y = 0
            else:
                x = tri[i][j - 1]
                y = tri[i][j]
            smol_tri.append(x + y)
        tri.append(smol_tri)
    return tri
