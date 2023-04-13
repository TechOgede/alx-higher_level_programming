#!/usr/bin/python3
''' This module defines a function that adds a new attriubte to an object '''


def add_attribute(obj, attr, value):
    ''' Adds a new attribute, key, and assigns value to it.
        If the object cant have new attriubte an exception is raised
    '''
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")

    setattr(obj, attr, value)
