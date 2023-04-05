#!/usr/bin/python3

"""Defines a Rectangle class"""


class Rectangle:
    """represent a rectangle"""

    def __init__(self, width=0, height=0):
        """initialise a new rectangle

        Attributes:
            width (int): The width of a new rectangle.
            height (int): The height of a new rectangle.
        """
        self.width = width
        self.height = height
    
    @property
    def width(self):
        """set the width of the rectangle"""
        return self.__width
    
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value
    
    @property
    def height(self):
        """set the height of the rectangle"""
        return self.__height
    
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
    
    def area(self):
        """return area of a rectangle."""
        return self.__width * self.__height
    
    def perimeter(self):
        """return perimeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)
    
    def __str__(self):
        """return a printable representation of a rectangle with a 3 character"""
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            rect = ""
            for i in range(self.__height):
                for j in range(self.__width):
                    rect += "#"
                if i != self.__height - 1:
                    rect += "\n"
            return rect
    
    def __repr__(self):
        """return the string representation of the rectangle"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

