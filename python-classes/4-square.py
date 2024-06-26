#!/usr/bin/python3
'''A class that defines a Square'''


class Square:
    '''Contains a private instance attribute of size with conditions'''

    def __init__(self, size=0):
        '''Contains a private attribute called size'''
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        '''Calcuates square area'''
        return self.__size ** 2

    @property
    def size(self):
        '''Retrieves itself'''
        return self.__size

    @size.setter
    def size(self, value):
        '''Determines whether the size is appropriate'''
        self.__size = value
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
