#!/usr/bin/python3
"""
A function that writes a string to a text file and returns
the number of chars written
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file and
    returns the no. of chars written
    """
    with open(filename, 'w') as file:
        chars_written = file.write(text)
        return chars_written
