#!/usr/python3

""" file Comments """


def matrix_divided(matrix, div):

    """ function Comments """

    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of list) of integers/floats")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new = []
    if matrix[0] is not list:
        raise TypeError("matrix must be a matrix (list of list) of integers/floats")
    num = len(matrix[0])
    for i in range(0, len(matrix)):
        new.append([])
        if type(matrix[i]) is not list:
            raise TypeError("matrix must be a matrix (list of list) of integers/floats")
        if num != len(matrix[i]):
            raise TypeError("Each row of the matrix must have the same size")

        for j in matrix[i]:
            if type(j) is not int and float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            new[i].append(round(j/div, 2))

    return new
