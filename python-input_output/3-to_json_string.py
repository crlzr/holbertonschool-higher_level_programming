#!/usr/bin/python3
"""
A function that returns the JSON representatoin of an object (string)
"""
import json


def to_json_string(my_obj):
    """
    returns the JSON rep of an object (string)
    """
    return json.dumps(my_obj)
