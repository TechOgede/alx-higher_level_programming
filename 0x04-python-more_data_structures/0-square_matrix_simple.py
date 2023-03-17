#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    sqrd_matrix = [[matrix[i][j] ** 2 for j in range(len(matrix[i]))]
                   for i in range(len(matrix))]
    return (sqrd_matrix)
