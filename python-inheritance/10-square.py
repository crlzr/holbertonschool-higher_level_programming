#!/usr/bin/python3
""" Nameless module containing BaseGeometry class """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    subclass Square
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        Calcuates area
        """
        return self.__size * self.__size

    def __str__(self):
        return str(Rectangle(self.__size, self.__size))
