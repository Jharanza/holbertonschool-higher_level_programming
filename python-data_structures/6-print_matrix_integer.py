#!/usr/bin/python3
''' Prints a matrix of integers '''

def print_matrix_integer(matrix=[[]]):
    for raw in matrix:
        for x in raw:
            print('{} '.format(x), end='') if x != raw[-1] else print(
                '{}'.format(x))
