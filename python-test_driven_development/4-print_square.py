#!/usr/bin/python3
"""
This function prints a square with the char #
"""


def print_square(size):
    """
    Args:
        size (int): length of the square sides.
    Returns:
        None: prints a square with the character '#'.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
