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
        """
        returns the product of width and height
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        returns the sum of all sides of a rectangle if width or height is not 0
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Prints the rectangle with the character #
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle_lines = ["#" * self.__width] * self.__height
        return "\n".join(rectangle_lines)
