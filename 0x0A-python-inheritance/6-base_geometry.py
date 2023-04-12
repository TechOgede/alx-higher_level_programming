#!/usr/bin/python3
''' This module defines a class, BaseGeometry.'''


class BaseGeometry:
    ''' Has only a single public instance method, area'''
    def area(self):
        ''' Raises an exception '''
        raise Exception('area() is not implemented')
