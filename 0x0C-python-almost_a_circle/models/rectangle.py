#!/usr/bin/python3
"""Defines a class Rectangle"""

from models.base import Base


class Rectangle(Base):
    """A Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """initializes a new instance

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
            x (int, optional): x coordinate of rectangle. Defaults to 0.
            y (int, optional): y coordinate of rectangle. Defaults to 0.
            id (_type_, optional): id of the rectangle. Defaults to None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """the getter for the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width

        Args:
            value (int): value for width attribute

        Raises:
            ValueError: if value is less or equal to 0
            TypeError: if value is not an integer
        """
        if type(value) != int:
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """Getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for height

        Args:
            value (int): value for height attribute

        Raises:
            ValueError: if value is less or equal to 0
            TypeError: if value is not an integer
        """
        if type(value) != int:
            raise TypeError("height must be an integer")

        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """Getter for x attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter for x

        Args:
            value (int): value for x attribute

        Raises:
            ValueError: if value is less or equal to 0
            TypeError: if value is not an integer
        """
        if type(value) != int:
            raise TypeError("x must be an integer")

        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """Getter for y attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter for y

        Args:
            value (int): value for y attribute

        Raises:
            ValueError: if value is less or equal to 0
            TypeError: if value is not an integer
        """
        if type(value) != int:
            raise TypeError("y must be an integer")

        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """returns the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """returns the display of the rectangle using the char '#"""
        for g in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x, end="")
            for j in range(self.__width):
                print("#", end='')
            print("")

    def __str__(self):
        """returns the string representation of the rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.__x, self.__y,
                                                       self.__width,
                                                       self.__height)

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute
        """
        if args:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.__width = arg
                elif i == 2:
                    self.__height = arg
                elif i == 3:
                    self.__x = arg
                elif i == 4:
                    self.__y = arg
                else:
                    pass
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "width":
                    self.__width = value
                elif key == "height":
                    self.__height = value
                elif key == "x":
                    self.__x = value
                elif key == "y":
                    self.__y = value
                else:
                    pass

    def to_dictionary(self):
        """"
        returns dictionary representation of a rectangle
        """
        return {
            "id": self.id,
            "width": self.__width,
            "height": self.__height,
            "x": self.__x,
            "y": self.__y,
        }
