#!/usr/bin/python3
''' This module defines a class Rectamngle. '''


from models.base import Base


class Rectangle(Base):
    ''' Represents a rectangle. Has private instance
        variables with public getter and setter methods
    '''
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)

        Rectangle.validator(width, height, x, y)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @classmethod
    def validator(cls, width, height, x, y):
        ''' Validates the types and values of the values to be set to attrs'''
        if type(width) is not int:
            raise TypeError('width must be an integer')
        if type(height) is not int:
            raise TypeError('height must be an integer')
        if type(x) is not int:
            raise TypeError('x must be an integer')
        if type(y) is not int:
            raise TypeError('y must be an integer')
        if width <= 0:
            raise ValueError('width must be > 0')
        if height <= 0:
            raise ValueError('height must be > 0')
        if x < 0:
            raise ValueError('x must be >= 0')
        if y < 0:
            raise ValueError('y must be >= 0')

    @property
    def width(self):
        ''' Getter for the private attr, width '''
        return self.__width

    @width.setter
    def width(self, value):
        ''' Setter for the private attr, width '''
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        ''' Getter for the private attr, height '''
        return self.__height

    @height.setter
    def height(self, value):
        ''' Setter for the private attr, width '''
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        ''' Getter for the private attr, x '''
        return self.__x

    @x.setter
    def x(self, value):
        ''' Setter for the private attr, x '''
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        ''' Getter for the private attr, y '''
        return self.__y

    @y.setter
    def y(self, value):
        ''' Setter for the private attr, y '''
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        ''' Returns the area of the rectangle '''
        return self.__width * self.__height

    def display(self):
        '''Prints the rectangle usiing #'''
        for h in range(self.__y):
            print()
        for i in range(self.__height):
            for k in range(self.__x):
                print(' ', end='')
            for j in range(self.__width):
                print('#', end='')
            print()

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}"\
            .format(self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        ''' Updates the values of the instance attrs'''
        if len(args) >= 1:
            if len(args) > 0:
                super().__init__(args[0])
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.height = args[2]
            if len(args) > 3:
                self.x = args[3]
            if len(args) > 4:
                self.y = args[4]
        else:
            for k, v in kwargs.items():
                if k == 'id':
                    super().__init__(v)
                if k == 'width' or k == 'size':
                    self.width = v
                if k == 'height' or k == 'size':
                    self.height = v
                if k == 'x':
                    self.x = v
                if k == 'y':
                    self.y = v

    def to_dictionary(self):
        ''' Returns the dictionary representation of the class '''
        return {'x': self.__x, 'y': self.__y, 'id': self.id,
                'height': self.__height, 'width': self.__width}

    def to_csv(self):
        ''' Returns the csv form of an object '''
        csv_ = []
        csv_.append(self.id)
        csv_.append(self.width)
        csv_.append(self.height)
        csv_.append(self.x)
        csv_.append(self.y)

        return csv_
