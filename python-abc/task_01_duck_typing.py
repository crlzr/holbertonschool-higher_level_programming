#!/usr/bin/env python3

"""
Abstract class Shape with abstract methods
"""

from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """
    Abstract class Shape
    """
    @abstractmethod
    def area(self):
        """
        Abstract method area
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Abstract method perimeter
        """
        pass


class Circle(Shape):
    """
    Subclass Circle
    """
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2

    def perimeter(self):
        return 2 * pi * self.radius


class Rectangle(Shape):
    """
    Subclass Rectangle
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Function to print the area and perimeter of a shape
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")


# Testing
circle = Circle(5)
rectangle = Rectangle(4, 7)


#shape_info(circle)
#shape_info(rectangle)
