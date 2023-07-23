#!/usr/bin/python3
'''
    2-square module
'''


class Square:
    ''' Square class '''

    def __init__(self, size=0):
        '''
            The __init__ method is a Constructor.
            Arguments:
                size (int): size of the square
        '''
        self.__size = size

        if int(size) < 0:
            raise ValueError("size must be >= 0")
        if not type(size) is int:
            raise TypeError("size must be an integer")
