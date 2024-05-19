#!/usr/bin/python3
"""
Module for rectancle class
"""


class Rectangle:
    """
    A class Rectangle
    """
    def __init__(self, width=0, height=0):
        """
        Attributes width and height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.area

    def perimeter(self):
        return self.perimeter

    if (width == 0) or (height == 0):
        perimeter = 0