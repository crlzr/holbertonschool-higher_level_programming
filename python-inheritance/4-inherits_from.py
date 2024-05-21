#!/usr/bin/python3
"""
Nameless module
"""


def inherits_from(obj, a_class):
    """
    Returns True if object is an instance of a class that
    inherited from the specified class, else False
    """
    if type(obj) is a_class:
        return False
    else:
        return isinstance(obj, a_class)
