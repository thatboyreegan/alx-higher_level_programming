#!/usr/bin/python3
"""Defines a function inherits_from()"""


def inherits_from(obj, a_class):
    """
    returns true or false depending on instance


    Args:
        obj (object): object
        a_class (class): class to inherit from

    Returns:
        tue if object is an instance of a class
    """
    if type(obj) is a_class:
        return False
    return issubclass(type(obj), a_class)
