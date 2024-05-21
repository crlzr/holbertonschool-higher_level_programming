#!/usr/bin/python3
"""
Module to return list of available attributes and methods of
an object
"""


def lookup(obj):
    """
    Function that returns the list of av. attributes
    and methods of object
    """
    return dir(obj)