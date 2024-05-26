#!/usr/bin/python3
"""
A function that appends a string at the end of a text file
and returns the number of chars
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file
    and returns the no. of chars
    """
    with open(filename, 'a') as file:
        chars_written = file.write(text)
    return chars_written
