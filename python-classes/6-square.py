#!/usr/bin/python3
'''
    module 6-square
'''


class Square:
    ''' class square '''

    def __init__(self, size=0, position=(0, 0)):
        '''
            Teh __init__ is the method Constructor.
            Args:
                size: The size of the square
        '''
        self.size = size
        self.__position = position

    @property
    def size(self):
        ''' The method getter to get the size of the square '''
        return self.__size

    @size.setter
    def size(self, value):
        ''' The method setter to set the size of the square '''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value <= 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        ''' The getter method get the position'''
        return self.__position

    @position.setter
    def position(self, value):
        ''' The setter method set he position with the valeu '''
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        x, y = value
        if not isinstance(x, int) or not isinstance(y, int) or x <= 0 or y <= 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        ''' The method area return the area of the square '''
        return self.__size * self.__size

    def my_print(self):
        ''' The method my_print print the coordinates of the square '''
        if self.__size == 0:
            print()

        x, y = self.__position

        for _ in range(y):
            print()

        for _ in range(self.__size):
            print("_" * x + "#" * self.size)
