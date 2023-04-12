#!/usr/bin/python3
''' This module defines a function that checks if an object is
    an instance of a class that inherited from a specified class'''


def inherits_from(obj, a_class):
    ''' Checks if an object is an instance of a class that inherited
        from a specified class
        Args:
            obj: the object
            a_class: the class which obj's class inherits
        Return:
            True if obj's class is a subclass of
            a_class(or any class which a_class inherits).
            Otherwise, False is returned.'''
    if type(obj) is not a_class:
        return issubclass(type(obj), a_class)
    return False
