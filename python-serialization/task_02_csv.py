#!/usr/bin/env python3
"""
Module that converts CSV data to JSON format.
"""

import csv
import json


def convert_csv_to_json(filename):
    """
    Converts CSV file data to JSON format and writes it to data.json.

    Args:
        filename (str): The CSV file to convert.

    Returns:
        bool: True if successful, False otherwise.
    """
    try:
        with open(filename, "r", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            data = [row for row in reader]

        with open("data.json", "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4)

        return True

    except Exception:
        return False
