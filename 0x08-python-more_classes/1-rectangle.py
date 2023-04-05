#!/usr/bin/python3
#1-rectangle.py
#Kelai137 of ALX

class Rectangle:
    """
    This class represents a rectangle object.
    
    A rectangle is defined by its length and width, which are both non-negative
    floating-point values.
    
    Attributes:
    - _width (int): the width of the rectangle
    - _height (int): the height of the rectangle
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
        return self._width
    
    @width.setter
    def width(self, value):
        """
        Sets the value of the width attribute to the given value.
        
        The width attribute must be an integer and must be >= 0, otherwise
        a TypeError or ValueError exception is raised.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self._width = value
    
    @property
    def height(self):
        """
        Retrieves the value of the height attribute.
        """
        return self._height
    
    @height.setter
    def height(self, value):
        """
        Sets the value of the height attribute to the given value.
        
        The height attribute must be an integer and must be >= 0, otherwise
        a TypeError or ValueError exception is raised.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self._height = value

     def area(self):
        """Return the area of the Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return the perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

     @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the Rectangle with the greater area.
        Args:
            rect_1 (Rectangle): The first Rectangle.
            rect_2 (Rectangle): The second Rectangle.
        Raises:
            TypeError: If either of rect_1 or rect_2 is not a Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

     @classmethod
    def square(cls, size=0):
        """Return a new Rectangle with width and height equal to size.
        Args:
            size (int): The width and height of the new Rectangle.
        """
        return (cls(size, size))

    def __str__(self):
        """Return the printable representation of the Rectangle.
        Represents the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")
        rect = []
        for i in range(self.__height):
            [rect.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        """Print a message for every deletion of a Rectangle."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
