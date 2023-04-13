#!/usr/bin/python3
''' This module defines the call, MyInt, which inherits int '''


class MyInt(int):
    ''' Rebel class. The functioonality of its ne and eq magic functions
        are inverted '''

    def __eq__(self, other):
        eq = int.__eq__(self, other)
        return not eq

    def __ne__(self, other):
        ne = int.__ne__(self, other)
        return not ne
