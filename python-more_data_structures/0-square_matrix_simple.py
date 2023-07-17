#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for fila in matrix:
        new_fila = [num ** 2 for num in fila]
        new_matrix.append(new_fila)
    return new_matrix
