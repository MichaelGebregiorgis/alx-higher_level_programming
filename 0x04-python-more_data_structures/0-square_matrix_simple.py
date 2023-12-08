#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    Square_matrix = []
    for column in matrix:
        value = list(map(lambda x: x**2, column))
        Square_matrix.append(value)
    return Square_matrix
