#!/usr/bin/python3
"""
This module provides a function that divides all elements of a matrix.
"""

import math


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by div and returns a new matrix.

    Args:
        matrix (list of lists): matrix of integers or floats.
        div (int or float): number to divide matrix elements by.

    Returns:
        list of lists: new matrix with divided values, rounded to 2 decimals.

    Raises:
        TypeError: if matrix is not a list of lists of integers/floats.
        TypeError: if each row is not the same size.
        TypeError: if div is not a number.
        ZeroDivisionError: if div is zero or inf/nan.
    """

    if not isinstance(div, (int, float)) or math.isnan(div) or math.isinf(div):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if (not isinstance(matrix, list) or
        not all(isinstance(row, list) for row in matrix) or
        not all(isinstance(num, (int, float)) for row in matrix for num in row)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    return [[round(num / div, 2) for num in row] for row in matrix]
