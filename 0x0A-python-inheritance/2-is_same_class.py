#!/usr/bin/python3
''' This module defines a function that checks if an object is
    exactly an instance of the specified class '''


def is_same_class(obj, a_class):
    ''' Checks if obj is an exact instance of a_class.
        i.e not checking for inheritance '''

    return type(obj) is a_class
