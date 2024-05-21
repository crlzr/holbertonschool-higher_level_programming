#!/usr/bin/python3
"""7-task"""


class BaseGeometry:
    """python3 -c 'print(__import__("my_module").MyClass.__doc__)'"""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not type(value) == int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))