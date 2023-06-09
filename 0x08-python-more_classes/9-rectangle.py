#!/usr/bin/python3
''' This module defines a Rectangle class '''


class Rectangle:
    ''' A Rectangle is a 2D shape that  consists of a width and a height '''

    number_of_instances = 0
    print_symbol = "#"

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        ''' returns the rectangle with the bigger area or\
          rect_1 if their areas are equal '''
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        rect_1_area = rect_1.area()
        rect_2_area = rect_2.area()
        if rect_1_area >= rect_2_area:
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        ''' Returns a new instance of Rectangle with width==height==size'''
        return cls(size, size)

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
        Rectangle.number_of_instances += 1

    def __str__(self):
        ''' Displays the rectangle using '#' '''
        string = ""
        if self.__height == 0 or self.__width == 0:
            pass
        else:
            for i in range(self.__height):
                for i in range(self.__width):
                    string += str(self.print_symbol)
                string += "\n"
        return string[:-1]

    def __repr__(self):
        ''' Returns a string that Python can parse and run as code '''
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print('Bye rectangle...')

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
