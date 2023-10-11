#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """function that computes the square value of all integers of a matrix."""
    new_mat = []
    for i in matrix:
        new_row = [x ** 2 for x in i]
        new_mat.append(new_row)
    return new_mat
