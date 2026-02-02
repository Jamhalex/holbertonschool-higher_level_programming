#!/usr/bin/python3
"""
Module that prints text with indentation.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after '.', '?' and ':'.

    Args:
        text (str): The text to print.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    separators = ".?:"
    line = ""

    for char in text:
        line += char
        if char in separators:
            print(line.strip())
            print()
            line = ""

    if line.strip():
        print(line.strip())
