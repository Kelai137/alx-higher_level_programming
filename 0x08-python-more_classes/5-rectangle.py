#!/usr/bin/python3

"""defines a rectangle class"""

class Rectangle:
    """represent a rectangle"""

    def __init__(self, width=0, height=0):
        """initialise a new rectangle.
        Attributes:
            width (int): the width of the ew rectangle.
            height (int): the height of the new rectangle
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
        """return the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """return the perimeter of the rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """return the print representation of the rectangle with # character"""
        if self.width == 0 or self.height == 0:
            return ""
        rect = ""
        for i in range(self.height):
            rect += "#" * self.width
            if i != self.height - 1:
                rect += "\n"
        return rect

    def __repr__(self):
        """return the string representation of the rectangle"""
        return "Rectangle({0}, {1})".format(self.width, self.height)

    def __del__(self):
        """print a message for every deletion of a rectangle"""
        print("Bye rectangle...")
