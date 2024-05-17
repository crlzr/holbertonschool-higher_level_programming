#!/usr/bin/python3
"""
add_integer: module that adds two integers together
"""

def add_integer(a, b=98):
    """
    A function that adds two integers

    Args:
        int a: The first integer to add.
        int b: The second integer to add, defaults to 98.

    Returns:
        The sum of a + b

    Raises:
        TypeError: If either a or b is not an integer.

    Unit tests: located in tests/0-add_integer.txt
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    return a + b
