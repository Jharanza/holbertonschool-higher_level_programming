#!/usr/bin/python3
'''
    module 4-rectangle that returns the width and the
    heigth of the rectangle
'''


class Rectangle:
    ''' class Rectangle that define a rectangle '''

    def __init__(self, width=0, height=0):
        '''
            method Constructor
            Args:
                width: The rectangle's width
                height: The rectangle's height
        '''
        self.width = width
        self.height = height

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

    def area(self):
        ''' method that defines the area of the rectangle '''
        return self.__width * self.__height

    def perimeter(self):
        ''' method that defines the perimeter of the rectangle '''
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        ''' method that represent the object in languaje human'''
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle_str = ""
        for _ in range(self.__height):
            rectangle_str += "#" * self.__width + "\n"
        return rectangle_str[:-1]

    def __repr__(self):
        ''' method that represent the object '''
        return f"Rectangle(width={self.__width}, height={self.__height})"
