#!/usr/bin/python3
''' This module defines a class that does not
    dynmaically create instance attributes unless
    the attribute name is 'first_name' '''


class LockedClass:
    ''' LockedClass uses the built-in class variable, __slots__
        to restrict names of instance variables to 'first_name'
        and 'first_name' alone '''
    __slots__ = ['first_name']

    def __init__(self):
        """ Init method """
        pass
