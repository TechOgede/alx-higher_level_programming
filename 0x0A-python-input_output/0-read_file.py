#!/usr/bin/python3
''' This module defines a function that
    reads a text file and prints it to stdout '''


def read_file(filename=""):
    ''' Takes a string as argument. The string denotes the filename '''
    with open(filename, "r", encoding='utf-8') as f:
        for line in f:
            print(line, end='')
