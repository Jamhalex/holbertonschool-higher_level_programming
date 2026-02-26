#!/usr/bin/env python3
"""
Module that provides basic JSON serialization
and deserialization functions.
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serializes a Python dictionary to JSON and saves it to a file.

    Args:
        data (dict): Dictionary to serialize.
        filename (str): Name of the file to save JSON data.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Loads JSON data from a file and deserializes it into a Python dictionary.

    Args:
        filename (str): Name of the file to read from.

    Returns:
        dict: The deserialized Python dictionary.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
