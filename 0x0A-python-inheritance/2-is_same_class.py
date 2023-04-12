#!/usr/bin/python3
"""Defines a function is_same_class()"""


def is_same_class(obj, a_class):
    """
    Returns True if obj is same instance as class

    Args:
        obj (object): object to be compared
        a_class (class): class to be compared
    """
    if type(obj) == a_class:
        return True
    return False
