#!/usr/bin/python3
"""
    Module 101-locked_class
    class LockedClass
"""


class LockedClass:
    """
    Prevents user from creating a new instance of a locked class
    for anything but attributes called "first_name"
    """
    __slots__ = "first_name"
