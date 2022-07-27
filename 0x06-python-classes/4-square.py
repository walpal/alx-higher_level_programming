#!/usr/bin/python3
"""class that defines a square with 
more Private instance attributes and
a Public instance method
"""


class Square:
    """Represents a square.
    Private instance attribute: size:
        - property def size(self)
        - property setter def size(self, value)
    Instantiation with optional size.
    Public instance method: def area(self).
    """

  def __init__(self, size=0):
        """Constructor of a Square with the size"""
        if (type(size) is not int):
            raise (TypeError("size must be an integer"))
        elif (size < 0):
            raise (ValueError("size must be >= 0"))
        else:
            self.__size = size

    def area(self):
        """Method to get the area of the Square"""
        return (self.__size ** 2)

    @property
    def size(self):
        """Getter of the private attribute size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Setter for the size private attribute"""
        if (type(value) is not int):
            raise (TypeError("size must be an integer"))
        elif (value < 0):
            raise (ValueError("size must be >= 0"))
        else:
            self.__size = value
