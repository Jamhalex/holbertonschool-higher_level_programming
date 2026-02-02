#!/usr/bin/python3
"""Module that prints a text with 2 new lines after '.', '?' and ':'."""


def text_indentation(text):
    """Print a text with 2 new lines after '.', '?' and ':'."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    separators = ".?:"
    chunk = ""

    for c in text:
        chunk += c
        if c in separators:
            # Print the sentence and exactly 2 new lines after it
            print(chunk.strip(), end="\n\n")
            chunk = ""

    # Print remaining text WITHOUT adding a final newline
    if chunk.strip():
        print(chunk.strip(), end="")
