#!/usr/bin/python3
''' This module defines a class, Rectangle.
    Rectangle inherits the class, BaseGeometry'''


class BaseGeometry:
    ''' Has two public instance methods, area() and integer_validator'''
    def area(self):
        ''' Raises an exception '''
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        if not isinstance(value, int) or not type(value) is int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))


class Rectangle(BaseGeometry):
    ''' Has two atrributes, width and height.
        They represent the sides of a rectange '''

    def __init__(self, width, height):
        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)
        self.__width = width
        self.__height = height
