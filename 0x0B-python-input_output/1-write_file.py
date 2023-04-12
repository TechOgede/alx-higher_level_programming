#!/usr/bin/python3
''' This module defines a function that
    writes a string to a  text file '''


def write_file(filename="", text=""):
    ''' Takes a string as argument. The string denotes the filename '''
    with open(filename, "w", encoding='utf-8') as f:
        num_chars_written = f.write(text)
    return num_chars_written
