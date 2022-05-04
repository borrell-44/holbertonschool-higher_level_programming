#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square = []
    if matrix:
        for i in range(0, len(matrix)):
            square.append([])
            for j in range(0, len(matrix[i])):
                square[i].append(matrix[i][j]**2)
        return square

    return square
