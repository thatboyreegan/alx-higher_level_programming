#!/usr/bin/python3
"""Defines function is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """
    compares an onject against a class

    Args:
        obj (object): object to be compared
        a_class (class): class to compare

    returns:
        true if obj is an instance of a class, false otherwise
    """
    if isinstance(obj, a_class):
        return True
    return False
