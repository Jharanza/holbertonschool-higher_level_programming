#!/usr/bin/python3
'''
    module 4-square
'''


class Square:
    ''' class square '''

    def __init__(self, size=0):
        '''
            Teh __init__ is the method Constructor.
            Args:
                size: The size of the square
        '''
        self.size = size

    @property
    def size(self):
        ''' The method getter to get the size of the square '''
        return self.__size

    @size.setter
    def size(self, value):
        ''' The method setter to set the size of the square '''
        if not type(value) is int:
            raise TypeError("size must be an integer")
        if int(value) < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        ''' The method area return the area of the square '''
        return int(self.__size) * int(self.__size)

    def my_print(self):
        if (self.__size) == 0:
            print()
        else:
            for x in range(self.__size):
                symbol = ""
                for y in range(self.size):
                    symbol += "#"
                print(symbol)
