#!/usr/bin/python3
'''
    Module 3-square
'''


class Square:
    ''' class square '''

    def __init__(self, size=0):
        '''
            The __init__ method is a Constructor.
            Args:
                size: size of the square
        '''
        self.__size = size

        if int(size) < 0:
            raise ValueError("size must be >= 0")
        if not type(size) is int:
            raise TypeError("size must be an integer")

    def area(self):
        ''' This method area return the area of the square '''
        return int(self.__size) * int(self.__size)
