#!/usr/bin/python3
""" Nameless module containing BaseGeometry class """


class BaseGeometry():
    """BaseGeometry Class.
    """

    def integer_validator(self, name, value):
        """validates value"""
        if type(value) is not int:
            raise TypeError("{0} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{0} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    sublcass Rectangle
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """returns area"""
        return (self.__width * self.__height)

    def __str__(self):
        """
        returns a string representation
        """
        return (f"[Rectangle] {self.__width}/{self.__height}")
