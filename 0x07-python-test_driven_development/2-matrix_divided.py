#!/usr/bin/python3
"""2-matrix_divided module."""


def matrix_divided(matrix, div):
    """Divide each elements of a list of lists by an int or float.

    args:
        matrix: the list of lists.
        div: the divisor.

    Return:
        A new list of list.
    """
    if (not matrix or type(matrix) is not list or len(matrix) == 0
            or any(not isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")

    length = len(matrix[0])
    for row in matrix:
        if len(row) != length:
            raise TypeError("Each row of the matrix must have the same size")

        if any(type(el) not in [int, float] for el in row):
            raise TypeError("matrix must be a matrix (list of lists)"
                            " of integers/floats")

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(el / div, 2) for el in row] for row in matrix]
