#!/usr/bin/python3
"""
Module to divide all elements of a matrix
"""

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a number.

    Args:
        matrix: List of lists of integers/floats
        div: Number to divide by (int or float)

    Returns:
        A new matrix with elements divided by div and rounded to 2 decimal places.

    Raises:
        TypeError: If matrix or div is of invalid type
        ZeroDivisionError: If div is zero

    Doctests:
    >>> matrix = [[1, 2, 3], [4, 5, 6]]
    >>> matrix_divided(matrix, 3)
    [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]

    >>> matrix_divided([[9, 12], [15, 18]], 3)
    [[3.0, 4.0], [5.0, 6.0]]

    >>> matrix_divided([[1.5, 2.5], [3.5, 4.5]], 2)
    [[0.75, 1.25], [1.75, 2.25]]

    >>> matrix_divided([[1, 2], [3]], 2)
    Traceback (most recent call last):
    TypeError: Each row of the matrix must have the same size

    >>> matrix_divided("not a matrix", 2)
    Traceback (most recent call last):
    TypeError: matrix must be a matrix (list of lists) of integers/floats

    >>> matrix_divided([[1, 2], [3, "four"]], 2)
    Traceback (most recent call last):
    TypeError: matrix must be a matrix (list of lists) of integers/floats

    >>> matrix_divided([[1, 2], [3, 4]], "two")
    Traceback (most recent call last):
    TypeError: div must be a number

    >>> matrix_divided([[1, 2], [3, 4]], 0)
    Traceback (most recent call last):
    ZeroDivisionError: division by zero
    """
    if (not isinstance(matrix, list) or
        not all(isinstance(row, list) for row in matrix) or
        not all(isinstance(el, (int, float)) for row in matrix for el in row)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(el / div, 2) for el in row] for row in matrix]
