#!/usr/bin/python3
"""
    Module to divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """matrix_divided divides all elements of a matrix.
    Args:
        matrix: list of lists of integers or floats
        div: a number (integer or float)
    Raises:
        TypeError: matrix must be a matrix (list of lists) of integers/floats
        TypeError: Each row of the matrix must have the same size
        TypeError: div must be a number
        ZeroDivisionError: exception with the message division by zero
    Return:
        Returns a new matrix
    """
    new_matrix = []
    Msg_Err1 = "matrix must be a matrix (list of lists) of integers/floats"
    Msg_Err2 = "Each row of the matrix must have the same size"
    if not matrix:
        raise TypeError(Msg_Err1)
    if not isinstance(matrix, list) or not all(
            isinstance(row, list) for row in matrix):
        raise TypeError(Msg_Err1)
    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError(Msg_Err2)
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(Msg_Err1)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for row in matrix:
        new_row = []
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(Msg_Err1)
            new_row.append(round((element / div), 2))
        new_matrix.append(new_row)
    return new_matrix
