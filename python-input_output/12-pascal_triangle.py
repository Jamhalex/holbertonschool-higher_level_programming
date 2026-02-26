#!/usr/bin/python3
"""
Module that defines a function to generate Pascal's triangle.
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing
    Pascal's triangle of n.
    """
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        row = [1]  # Every row starts with 1

        if triangle:
            prev_row = triangle[-1]
            for j in range(1, len(prev_row)):
                row.append(prev_row[j - 1] + prev_row[j])
            row.append(1)  # Every row ends with 1

        triangle.append(row)

    return triangle
