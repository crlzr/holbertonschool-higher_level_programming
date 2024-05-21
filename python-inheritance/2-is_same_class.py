#!/usr/bin/python3
"""
A function that returns True if the object is exactly an instance of
the specified class; otherwise False
"""


def is_same_class(obj, a_class):
    """
    Returns True if object is exactly an instance
    of specified class, else False
    """
    if isinstance(obj, a_class):
        return type(obj) == a_class
