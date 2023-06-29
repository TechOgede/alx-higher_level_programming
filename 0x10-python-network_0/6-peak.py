#!/usr/bin/python3
''' This module defines a function that
    determines the peak of an array of its
'''


def find_peak(list_of_integers):
    '''Determines the peak of an array of ints '''
    if not list_of_integers:
        return

    _list = list_of_integers
    size = len(_list)

    if _list[0] > _list[1]:
        return _list[0]
    elif _list[size - 1] > _list[size - 2]:
        return _list[size - 1]
    else:
        for i in range(1, size):
            if _list[i] >= _list[i + 1] and _list[i] >= _list[i - 1]:
                return _list[i]
