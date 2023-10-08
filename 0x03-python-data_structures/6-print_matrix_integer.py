#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """function that prints a matrix of integers."""
    for i in matrix:
        for j in i:
            print(j, end =" ")
        print("$")
