#!/usr/bin/python3
"""Defines a function that divides a all the elemnts of a matrix"""


def matrix_divided(matrix, div):
    """
    Divides all the elements of a matrix and returns the result in a new matrix

    Args:
        matrix: A matrix
        div(int/float): divisor

    Raises:
        TypeError: when matrix contains non-numbers.
        TypeError: when matrix contains rows of different sizes.
        TypeError: when div is not an int or float.
        ZeroDivisionError: when div is 0.
    """
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    size = len(matrix[0])
    for array in matrix:
        if len(array) != size:
            raise TypeError("Each row of the matrix must have the same size")
        for element in array:
            if not isinstance(element, int) or isinstance(element, float):
                err = ("matrix must be a matrix (list of lists) of integers/")
                raise TypeError(err + "floats")

    new_matrix = []
    for array in matrix:
        new_array = []
        for element in array:
            new_array.append(round(element / div, 2))
        new_matrix.append(new_array)

    return new_matrix
