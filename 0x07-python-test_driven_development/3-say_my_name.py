#!/usr/bin/python3
"""Defines a function that prints names given by a user"""


def say_my_name(first_name, last_name=""):
    """
    Prints a name given(first name and last name)

    Args:
        first_name: first string
        last_name: second string

    Raises:
        TypeError: when either args are not strings
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
