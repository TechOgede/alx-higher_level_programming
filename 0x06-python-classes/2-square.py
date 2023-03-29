#!/usr/bin/python3
''' This Module defines a Square class. It has one private instance
    variable, size.'''


class Square:
    ''' This class has one private instance variable'''
    def __init__(self, size=0):
        '''Args:
            size (int): positive integer. Denotes the size of a square.
        '''
        self.__size = size
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")
