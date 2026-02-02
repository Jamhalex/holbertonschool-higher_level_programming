#!/usr/bin/python3
"""Module that finds the max integer in a list."""


def max_integer(list=[]):
    """Return the max integer in a list.

    If the list is empty, return None.
    """
    if list == []:
        return None

    max_value = list[0]
    for i in list:
        if i > max_value:
            max_value = i
    return max_value
