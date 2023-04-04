#!/usr/bin/python3
''' This module defines a function that divides each memeber of a matrix
by another number '''


def matrix_divided(matrix, div):
    ''' Divides every memeber of matrix by div
        Args:
         matrix: must be a list of lists of integers/floats
                 of which each row must be of the same size
         div (int) or (float): cannot be 0
        Returns:
         A new matrix with each element rounded to 2 decimal places
    '''
    if not isinstance(matrix, list) or not matrix:
        raise TypeError("matrix must be a matrix" +
                        "(list of lists) of integers/floats")

    len_list_ = 0
    for list_ in matrix:
        if not isinstance(list_, list) or not list_:
            raise TypeError("matrix must be a matrix" +
                            "(list of lists) of integers/floats")
        len_list_ = len(matrix[0])
        if len_list_ != len(list_):
            raise TypeError('Each row of the matrix must have the same size')
        for value in list_:
            if not isinstance(value, int) and not isinstance(value, float):
                raise TypeError("matrix must be a matrix" +
                                "(list of lists) of integers/floats")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')

    m = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))

    return m
