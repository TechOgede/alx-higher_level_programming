#!/usr/bin/python3
''' This module defines a class, Student'''


class Student:
    ''' Defines a student. Has first name, last name, and age as attributes.
        Also posesses a method that returns a dict description of instance '''
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        ''' Returns a dict description of the instance '''
        if type(attrs) is list:
            list_of_strings = True
            desc = {}
            for attr in attrs:
                if type(attr) is not str:
                    list_of_strings = False
                if attr in self.__dict__:
                    desc[attr] = self.__dict__[attr]
            if list_of_strings:
                return desc
        return self.__dict__.copy()
