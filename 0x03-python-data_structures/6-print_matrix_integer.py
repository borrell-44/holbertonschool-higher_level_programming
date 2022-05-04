#!/usr/bin/python3
def print_matrix_integer(matrix=[]):
    if not matrix or matrix is None:
        print()
    else:
        for i in matrix:
            print(*f"{i}", sep=" ")
'''
            for j in range(0, len(matrix)):
                print("{:d}".format(matrix[i][j]), end="")
                print(" " if j != len(matrix[i]) - 1 else "\n", end="")
'''
