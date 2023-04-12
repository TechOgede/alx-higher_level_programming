#!/usr/bin/python3
''' This module defines a class, Student'''


class Student:
    ''' Defines a student. Has first name, last name, and age as attributes.
        Also posesses a method that returns a dict description of instance '''
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        ''' Returns a dict description of the instance '''
        return self.__dict__.copy()
