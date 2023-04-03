#!/usr/bin/python3
''' This module defines a Rectangle class '''


class Rectangle:
    ''' A Rectangle is a 2D shape that  consists of a width and a length '''
    def __init__(self, width=0, height=0):
        ''' Initialises the parameters of a rectangle
        Args:
         width (int): width of rectangle
         height (int): height of rectangle '''
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        if width < 0:
            raise ValueError('width must be >= 0')
        self.__width = width
        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        if height < 0:
            raise ValueError('height must be >= 0')
        self.__height = height

    @property
    def width(self):
        ''' Getter for the width attribute '''
        return self.__width

    @width.setter
    def width(self, value):
        ''' Setter for the width attribute '''
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        ''' Getter for the height attribute '''
        return self.__height

    @height.setter
    def height(self, value):
        ''' Setter for the height attribute '''
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        ''' Calculates the area of the rectangle '''
        return self.__width * self.__height

    def perimeter(self):
        ''' Calculates the perimeter of the rectangle '''
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
