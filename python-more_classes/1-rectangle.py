#!/usr/bin/python3
''' module 1-rectangle that returns the width and the heigth of the rectangle '''


class Rectangle:
    ''' class Rectangle that define a rectangle '''

    def __init__(self, width=0, height=0):
        '''
            method Constructor
            Args:
                width: The rectangle's width
                height: The rectangle's height
        '''
        self.__width = width
        self.__height = height

    ''' Methods setters and getters of width '''
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise TypeError("width must be >= 0")
        self.__width = value

    ''' Methods setter and getter of height '''
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise TypeError("height must be >= 0")
        self.__height = value
