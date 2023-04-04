#!/usr/bin/python3
''' this module defines a function that prints a square using '#' '''


def print_square(size):
    ''' Prints a square of size, size using '#'
        Args:
         size (int): size >= 0
    '''

    if isinstance(size, float) and size < 0:
        raise TypeError('size must be an integer')
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')

    for i in range(size):
        for k in range(size):
            print('#', end='')
        print()
