#!/usr/bin/python3
"""
Module that defines a function to check if an object is
an instance of a class or inherited from it.
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if obj is an instance of a_class
    or of a class that inherited from a_class,
    otherwise False.
    """
    return isinstance(obj, a_class)
