#!/usr/bin/python3
"""Moduke defines the class Rectangle"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class Rengtang ethat inherits from BaseGeometry"""

    def __init__(self, width, height):
        """
        initializes a new instance of the class Rectangle

        Args:
            width(int): the width of the rectange
            height(int): the height of the rectange
        """
        super().__init__()

        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
