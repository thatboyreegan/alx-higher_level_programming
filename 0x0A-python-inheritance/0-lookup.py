#!/usr/bin/python3
"""Module for looking up an object"""


def lookup(obj):
    """
    defines the lookup function

    Args:
        obj (all): _object to look up

    Returns:
        list : a list of available attributes and methods of an onject
    """
    return dir(obj)
