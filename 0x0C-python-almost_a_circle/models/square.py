#!/usr/bin/python3
''' This module defines a class, Square '''


from models import rectangle


class Square(rectangle.Rectangle):
    ''' Template for a Square object. Inherits rectangle.Rectangle '''
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return '[Square] ({}) {}/{} - {}'\
            .format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        ''' Getter for size '''
        return self.width

    @size.setter
    def size(self, value):
        ''' Setter for size '''
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        ''' Updates the values of the instance attrs'''
        if len(args) >= 2:
            args_list = list(args)
            args_list.insert(1, args[1])
            args = tuple(args_list)
        super().update(*args, **kwargs)

    def to_dictionary(self):
        ''' Returns the dictionary representation of a Square object '''
        return {'id': self.id, 'size': self.size, 'x': self._Rectangle__x,
                'y': self._Rectangle__y}

    def to_csv(self):
        ''' Returns the csv form of an object '''
        csv_ = []
        csv_.append(self.id)
        csv_.append(self.size)
        csv_.append(self.x)
        csv_.append(self.y)

        return csv_
