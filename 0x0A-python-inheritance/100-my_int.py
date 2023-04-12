#!/usr/bin/python3
"""Defines a class Myint"""


class Myint(int):
    """Inherits from int class"""
    def __init__(self, value):
        """
        initializes an instance of Myint

        Args:
            Value: The value to set
        """
        self.value = value

    def __ne__(self, other):
        """Returns true or false

        Args:
            other(obj): The value to compare with the instance
        """
        if self.value is other:
            return True

    def __eq__(self, other):
        """chechs for equality or lack of between two integers

        Args:
            other(obj): The value to compare with the instance

        Returns:
            true if values are equal, else false
        """
        return not self.__ne__(other)
