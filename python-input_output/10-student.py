#!/usr/bin/python3
"""
write a class Student that defines a student
"""


class Student:
    """
    A class named Student
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        public method to retrieve the dict rep. of a student
        instance - with conditions
        """
        dict = {}

        if attrs is None:
            return vars()
        else:
            for key in attrs:
                if key in self.__dict__:
                    dict[key] = self.__dict__[key]
            return dict
