#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square_matrix = []
    for x in range(10):
       new_matrix = matrix
       square_matrix.append(x**2)
       matrix = (map(lambda x: x**2, range(10)))
       return new_matrix
