#!/usr/bin/python3
''' This module defines a function that returns the sum of two integers '''


def add_integer(a, b=98):
    ''' this function takes in two integers and returns their sum
        Args:
         a (int) or (float)
         b (int) or (float)
         if a or b is float, it is first casted to an int
        Returns:
         the sum of a and b as an integer '''
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
