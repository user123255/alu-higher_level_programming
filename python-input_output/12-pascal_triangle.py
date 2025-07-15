#!/usr/bin/python3
"""Function to generate Pascal's Triangle."""


def pascal_triangle(n):
    """Return a list of lists representing Pascal’s triangle of n."""
    if n <= 0:
        return []

    triangle = [[1]]  # First row

    for i in range(1, n):
        prev_row = triangle[-1]
        row = [1]  # First element of the row
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])  # Middle elements
        row.append(1)  # Last element of the row
        triangle.append(row)

    return triangle
