#!/usr/bin/python3
"""An class Square that defines a square by private instance attribute: size"""

class Square:
    def __init__(self, size=0):
        if not type(int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
