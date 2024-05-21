#!/usr/bin/python3
"""
Nameless module
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if object is instance of or instance of
    a class that inherited from the specified class,
    else False
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
