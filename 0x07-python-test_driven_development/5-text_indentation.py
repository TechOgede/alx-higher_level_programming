#!/usr/bin/python3
''' this module defines a function that accepts text as argument and prints
    two new lines after each ., ? or :
'''


def text_indentation(text):
    ''' Prints two new lines after each ., ? or : in a text string
        Args:
         text (str)
    '''

    if not isinstance(text, str):
        raise TypeError('text must be a string')

    line = text[:]  #copying the string
    string = ""
    i = 0
    while i < len(line):
        if line[i] in ['.', '?', ':']:
            string += line[: i + 1]
            print(string.strip())
            print()
            line = line[i + 1:]
            string = ""
            i = 0
        else:
            i += 1
    string += line
    print(string.strip(), end='')
    return
