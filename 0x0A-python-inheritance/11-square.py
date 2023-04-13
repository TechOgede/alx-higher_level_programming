#!/usr/bin/python3
''' This module defines a class, Square, that inherits the class, Rectangle '''


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    ''' Inherits Rectangle. Has its own area method.
        One private instance variable '''
    def __init__(self, size):
        self.integer_validator("size", size)
        Rectangle.__init__(self, size, size)
        self.__size = size

    def area(self):
        ''' Returns the area of the square '''
        return self.__size * self.__size

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
