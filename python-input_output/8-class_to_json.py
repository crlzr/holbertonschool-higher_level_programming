#!/usr/bin/python3
"""
Write a function that returns the dictionary
description with simple data structure (list, string, integer, boleean)
for JSON serialization of an object
"""


def class_to_json(obj):
    """
    a function that returns the dict description with
    simple data structure
    """
    return obj.__dict__
