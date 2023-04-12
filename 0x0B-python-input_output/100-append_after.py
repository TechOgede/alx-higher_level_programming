#!/usr/bin/python3
''' This module defines a function that inserts a new line of text
    right after a line that contains a specfic string '''


def append_after(filename="", search_string="", new_string=""):
    ''' Inserts 'new_string' after each line containing 'search_string'
    '''
    indices = []
    with open(filename, "r", encoding='utf-8') as f:
        lines = f.readlines()
        for i in range(len(lines)):
            if search_string in lines[i]:
                indices.append(i)
        for index in indices:
            lines[index] += new_string

    with open(filename, "w", encoding='utf-8') as f:
        f.writelines(lines)
    return
