#!/usr/bin/python3
"""Defines a function that prints a square"""


def print_square(size):
    """
    Prints a square with "#"

    Args:
        size(int/float): size of the square

    Raises:
        TypeError:when size is not an int or float
        ValueError:when size is less than 0
    """
    if type(size) is not int and type(size) is not float:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")
    print("")
