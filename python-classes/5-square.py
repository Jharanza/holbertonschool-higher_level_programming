#!/usr/bin/python3
""" Create a Square class with a method to print the square"""

class Square:

    def __init__(self, size=0) -> None:
        """ Constructor """
        self.__size = size

    @property        
    def size(self):
        """ Getter """
        return self.__size

    @size.setter
    def size(self, value):
        """ Setter"""
        if type(value) != int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self) -> int:
        """ Returns the square area """
        return self.__size * self.__size

    def my_print(self):
        """ Print the square """
        if self.__size == 0:
            print('')
        else:
            for _ in range(self.__size):
                print('#' * self.__size)
