#!/usr/bin/python3
"""Module for class BaseGeometry"""


class BaseGeometry:
    """class BaseGeometry"""

    def area(self):
        """
        Raises an exception

        Raises:
            Exception : Always...
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates a value

        Args:
            name (str): string whose value is to be assigned
            value (int): the integer thatis to be assigned

        Raises:
            TypeError: If the value is not an integer
            ValueError: If the value is less or equal to 0
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
