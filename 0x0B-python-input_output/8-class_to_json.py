#!/usr/bin/python3
''' This module defines a function that returns the dictionary description
    of an instance '''


def class_to_json(obj):
    ''' Returns a copy of the instances's __dict__ attribute '''
    return obj.__dict__.copy()
