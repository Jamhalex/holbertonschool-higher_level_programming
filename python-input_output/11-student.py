#!/usr/bin/python3
"""
Module that defines a Student class with JSON serialization and reloading.
"""


class Student:
    """
    Student class with JSON export and reload support.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialize a Student instance.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns the dictionary representation of the instance.

        If attrs is a list of strings, only those attributes are included.
        Otherwise, all attributes are returned.
        """
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            return {key: self.__dict__[key]
                    for key in attrs
                    if key in self.__dict__}
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance from a dictionary.
        """
        for key, value in json.items():
            setattr(self, key, value)
