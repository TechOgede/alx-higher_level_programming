#!/usr/bin/python3
''' This module defines a class, Rectangle.
    Rectangle inherits the class, BaseGeometry'''


BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    ''' Has two atrributes, width and height.
        They represent the sides of a rectange '''

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
