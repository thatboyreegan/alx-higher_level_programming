#!/usr/bin/python3
"""Defines a function add_attribute"""


def add_attribute(obj, name, value):
    """
    Add a new attribute to an object if at all possible

    Args:
        obj(object): The object to add attribute to.
        name(str): The name of the attribute
        value(str): The value of the attribute
    Raises:
        TypeError: If the attribute cant be added
    """
    if '__dict__' not in dir(obj):
        raise TypeError("can't add new attribute")
    obj.__dict__[name] = value
