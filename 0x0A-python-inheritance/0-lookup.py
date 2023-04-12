#!/usr/bin/python3
''' This module defines a function that returns a list of all
    attributes and methods in a class '''


def lookup(object):
    ''' returns a list of all attributes and methods in a class '''
    return dir(object)
