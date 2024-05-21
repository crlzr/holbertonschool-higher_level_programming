#!/usr/bin/python3
"""
Module for rectangle class
"""

class Rectangle:
    """
    A class Rectangle
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Attributes width and height
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        rectangle_lines = [str(self.print_symbol) * self.__width] * self.__height
        return "\n".join(rectangle_lines)

    def __repr__(self):
        """
        return a string representation of the rectangle
        with which we can recreate a new instance by using eval()
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

# Example usage
if __name__ == "__main__":
    my_rectangle_1 = Rectangle(8, 4)
    print(my_rectangle_1)
    my_rectangle_1.print_symbol = "H"
    print(my_rectangle_1)

    my_rectangle_2 = Rectangle(2, 1)
    print(my_rectangle_2)
