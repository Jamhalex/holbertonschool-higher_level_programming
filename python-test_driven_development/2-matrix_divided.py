#!/usr/bin/python3
"""
Module that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by div, rounded to 2 decimals.

    Args:
        matrix (list of lists): matrix of integers/floats
        div (int/float): divisor

    Returns:
        list of lists: new matrix with results rounded to 2 decimals

    Raises:
        TypeError: if matrix is not a matrix of ints/floats
        TypeError: if rows are not the same size
        TypeError: if div is not a number
        ZeroDivisionError: if div == 0
    """
    # Validate div
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Validate matrix structure and content
    if (not isinstance(matrix, list) or matrix == [] or
            any(not isinstance(row, list) or row == [] for row in matrix)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_len = len(matrix[0])
    for row in matrix:
        if len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")
        for item in row:
            if not isinstance(item, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Build and return new divided matrix
    return [[round(item / div, 2) for item in row] for row in matrix]
