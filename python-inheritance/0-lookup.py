#!/usr/bin/python3
"""
Module that defines a function lookup.
"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.
    """
    return dir(obj)
