#!/usr/bin/python3
"""Defines a class Square"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """A square"""
    def __init__(self, size, x=0, y=0, id=None):
        """initializes a new instance

        Args:
            size (int): size of the square
            x (int, optional): x coordinate of the square. Defaults to 0.
            y (int, optional): y coordinate of the square. Defaults to 0.
            id (int, optional): id of the square. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter for the size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """setter for the size of the square

        Args:
            value(int): value of the size of the square
        Raises:
            ValueError: if the value of size is less or equal to 0
            TypeError: if the value of size is not an integer
        """
        if type(value) != int:
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.width = value
        self.height = value

    def __str__(self):
        """
        returns the string representation of the square
        """
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """
        assigns an argument to each attribute
        """
        if args:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
                else:
                    pass
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value
                else:
                    pass

    def to_dictionary(self):
        """"
        returns dictionary representation of a square
        """
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y,
        }
