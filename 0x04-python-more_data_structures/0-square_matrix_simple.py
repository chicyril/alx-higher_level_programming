#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """Squares each elements in a nested list."""

    return ([[el ** 2 for el in row] for row in matrix])
