#!/usr/bin/python3
''' A class that defines a square'''


class Square:
    ''' Contains a private instance attribute named size'''
    def __init__(self, size=0):
        ''' private attribute size'''
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        '''Determines whether the size is appropriate'''
        self.__size = value
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        '''returns the current square area'''
        return self.__size ** 2

    def my_print(self):
        ''' prints to stdout the square with the character #'''
        if self.size == 0:
            print()
        else:
            for i in range(self.size):
                print("#" * self.size)
