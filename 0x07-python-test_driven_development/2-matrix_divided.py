#!/usr/bin/python3
"""Division function"""


def matrix_divided(matrix, div):
    """Divide values inside the matrix"""
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if (matrix == [] or not isinstance(matrix, list) or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, float) or isinstance(ele, int))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
