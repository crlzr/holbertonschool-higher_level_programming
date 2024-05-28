#!/usr/bin/python3
"""
Serialize and De-serialize using pickle module
"""
import pickle


class CustomObject:
    """
    A class called CustomObject
    """

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Print out object's attributes
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Takes a filename as parameter and will
        serialize the current instance of the object
        and save it to the provided filename
        """
        with open(filename, 'wb') as file:
            pickle.dump(self, file)

    @classmethod
    def deserialize(cls, filename):
        """
        Class method that takes a filename as its
        parameter. It will load and return an instance
        of the CustomObject from the provided
        filename
        """
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except FileNotFoundError:
            print("Specified file not found!")

        return None
