#!/usr/bin/python3
''' This module defines a function that creates Pascal triaangle '''


def pascal_triangle(n):
    ''' Creates a Pascal triangle up to n
        Args:
            n (int): should be > 0
        Returns:
            Pasccal triangle as a list of lists of integers
    '''
    pascal = []

    if n > 0:
        for i in range(1, n+1):
            row = []
            if i < 3:
                for k in range(i):
                    row.append(1)
                pascal.append(row)
            else:
                prev = pascal[-1]
                row.append(1)
                for j in range(len(prev) - 1):
                    row.append(prev[j] + prev[j+1])
                row.append(1)
                pascal.append(row)
    return pascal
