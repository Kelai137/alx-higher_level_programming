#!/usr/bin/python3
"""contains class rectangle
with private attribute of width and height
"""

class Rectangle:
    """
    This class represents a rectangle object.
    
    A rectangle is defined by its length and width, which are both non-negative
    floating-point values.
    
    Attributes:
    - __width (int): the width of the rectangle
    - __height (int): the height of the rectangle
    """
    
    def __init__(self, width=0, height=0):
        """
        Initializes a new rectangle object with the given width and height.
        The default values for width and height are both 0.
        """
        self.width = width
        self.height = height
        
    @property
    def width(self):
        """
        Retrieves the value of the width attribute.
        """
        return self.__width
    
    @width.setter
    def width(self, value):
        """
        Sets the value of the width attribute to the given value.
        
        The width attribute must be an integer and must be >= 0, otherwise
        a TypeError or ValueError exception is raised.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value
    
    @property
    def height(self):
        """
        Retrieves the value of the height attribute.
        """
        return self.__height
    
    @height.setter
    def height(self, value):
        """
        Sets the value of the height attribute to the given value.
        
        The height attribute must be an integer and must be >= 0, otherwise
        a TypeError or ValueError exception is raised.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
