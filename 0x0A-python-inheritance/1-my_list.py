#!/usr/bin/python3
''' This module defines a class that inherits from the 'list' class '''


class MyList(list):
    ''' MyList inherits attributes and methods from the built-in class, list'''
    def __init__(self):
        list.__init__(self)

    def print_sorted(self):
        ''' prints the items of a MyList object sorted in ascending order '''
        print(sorted(self))
