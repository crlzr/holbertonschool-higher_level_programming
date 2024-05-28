#!/usr/bin/python3
"""
A basic serialization module
"""
import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize data to the specified file.

    Args:
    data: Python dict with data.
    filename: Filename of the output JSON file.
    """
    with open(filename, 'w') as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """
    Load and deserialize data from the specified file.

    Args:
    filename: Filename of the JSON file to read.

    Returns:
    The deserialized Python dict.
    """
    with open(filename, 'r') as file:
        return json.load(file)
