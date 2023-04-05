#!/usr/bin/python3
"""defines a rectangle class"""

class Rectangle:

    def __init__(self, width=0, height=0):
        """initialises a new rectangle.
        Attributes:
            width (int) : the width of a new rectangle
            height (int) : the height of a new rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """retrieves width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieves the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """return the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """return perimeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """return the print representation of the rectangle with the # character"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        else:
            rect = []
            for i in range(self.__height):
                [rect.append('#') for j in range(self.__width):
                if i != self.__height - 1:
                    rect.append("\n")
            return ("".join(rect))
