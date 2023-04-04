#!/usr/bin/python3
"""Defines a function that adds tow integers"""


def add_integer(a, b=98):
    """
    Adds two integers and returns the result

    Args:
        a(int): The first integer to add
        b(int): The second integer to add

    Raises:
        TypeError: when either a or b is not a n int/float
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)

    return a + b
