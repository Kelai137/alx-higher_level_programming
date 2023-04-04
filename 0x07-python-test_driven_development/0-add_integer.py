#!usr/bin/python3
"""
This module contains a function that adds two integers
"""

def add_integer(a, b=98):
    """Return the integer value addition of the integers a and b.
    Float arguments are typecasted to ints before the addition takes place.
    Raises:
        TypeError: If a is non-int or non-float or b is a non-int or non-float.
    """

    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
