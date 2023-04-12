#!/usr/bin/python3
"""Defines a mudule that has class Mylist"""


class MyList(list):
    """Defines class Mylist"""

    def print_sorted(self):
        """Prints a sorted list"""
        print(sorted(self))
