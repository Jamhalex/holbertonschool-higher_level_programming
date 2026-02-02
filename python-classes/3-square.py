#!/usr/bin/python3
"""Defines a Square class with validated size and area calculation."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initialize a Square with a private size."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current area of the square."""
        return self.__size * self.__size
