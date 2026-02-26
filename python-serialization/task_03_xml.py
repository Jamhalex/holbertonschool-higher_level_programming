#!/usr/bin/env python3
"""
Module that provides XML serialization and deserialization functions.
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serializes a Python dictionary to XML and saves it to a file.

    Args:
        dictionary (dict): Dictionary to serialize.
        filename (str): Output XML filename.
    """
    try:
        root = ET.Element("data")

        for key, value in dictionary.items():
            child = ET.SubElement(root, key)
            child.text = str(value)

        tree = ET.ElementTree(root)
        tree.write(filename, encoding="utf-8", xml_declaration=False)

    except Exception:
        return None


def deserialize_from_xml(filename):
    """
    Deserializes an XML file into a Python dictionary.

    Args:
        filename (str): XML file to read.

    Returns:
        dict: Deserialized dictionary or None if error.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        result = {}
        for child in root:
            result[child.tag] = child.text

        return result

    except Exception:
        return None
