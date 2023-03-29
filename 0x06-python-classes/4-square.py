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

    @property
    def size(self):
        ''' Getter for the size
        Returns:
          an integer. the size variable'''
        return self.__size

    @size.setter
    def size(self, value):
        ''' Setter for the priv var, size
        Args:
          value: value to which size is updated'''
        self.__size = value
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        ''' Calculates the area of the square
            Returns:
              an integer
        '''
        return self.__size * self.__size
