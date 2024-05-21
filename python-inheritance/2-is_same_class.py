#!/usr/bin/python3
"""
??
"""


def is_same_class(obj, a_class):
    """
    Returns True if object is exactly an instance
    of specified class
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
