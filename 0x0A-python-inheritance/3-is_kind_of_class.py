#!/usr/bin/python3
''' This module defines a function that checks if an object is
    exactly an instance of the specified class or if its an
    of an inherited class'''


def is_same_class(obj, a_class):
    ''' Checks if an object is an instance of a class or an inherited class
        Args:
            obj: the object
            a_class: the class or any class which a_class inherits
        Return:
            True if obj is an instance of
            a_class(or any class which a_class inherits).
            Otherwise, False is returned.'''
    return isinstance(obj, a_class)
