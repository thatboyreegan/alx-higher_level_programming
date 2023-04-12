#!/usr/bin/python3
"""Defines a  class Square"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class Square that inherits from class Rectangle"""

    def __init__(self, size):
        """initializes an instance of the class

        Args:
            size (int): size of the square
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def __str__(self):
        """returns the string representation of square"""
        return "[sqaure] {}/{}".format(self.__size, self.__size)
