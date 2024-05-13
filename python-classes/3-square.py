#!/usr/bin/python3

'''A class Square that defines a square '''


class Square:
    ''' Contains a private instance variable (also called attribute: size)'''
    def __init__(self, size=0):
        self.__size = size

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif type < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return self.__size ** 2
