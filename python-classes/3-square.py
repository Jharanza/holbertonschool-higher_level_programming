#!/usr/bin/python3
""" Create a Square class with a method that returns its square area"""

class Square:
    
    def __init__(self, size=0) -> None:
        """ Constructor """
        if type(size) != int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self) -> int:
        """ Returns the square area """
        return self.__size * self.__size
