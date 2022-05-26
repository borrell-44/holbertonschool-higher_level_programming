#!/usr/bin/python3

""" file Comments """


def matrix_divided(matrix, div):

    """ function Comments """

    string1 = "matrix must be a matrix (list of list) of integers/floats"
    string2 = "matrix must be a matrix (array of arrays of integers/floats)"
    if type(matrix) is not list:
        raise TypeError(string1)

    if type(div) is not int and float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new = []
    if type(matrix[0]) is not list:
        raise TypeError(string1)
    num = len(matrix[0])
    for i in range(0, len(matrix)):
        new.append([])
        if type(matrix[i]) is not list:
            raise TypeError(string1)
        if num != len(matrix[i]):
            raise TypeError("Each row of the matrix must have the same size")

        for j in matrix[i]:
            if type(j) is not int and float:
                raise TypeError(string2)
            new[i].append(round(j/div, 2))

    return new
