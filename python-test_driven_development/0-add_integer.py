#!/usr/bin/python3
"""Module that adds two integers."""


def add_integer(a, b=98):
    """Return the addition of a and b as integers.

    a and b must be integers or floats.
    Floats are casted to integers before addition.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Reject NaN values (float overflow case)
    if a != a:
        raise TypeError("a must be an integer")
    if b != b:
        raise TypeError("b must be an integer")

    return int(a) + int(b)

