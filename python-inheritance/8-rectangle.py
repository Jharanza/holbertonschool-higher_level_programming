#!/usr/bin/python3
''' Module 8-rectangle that inherits methods of BaseGeometry '''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    ''' class Rectangle with constructor '''

    def __init__(self, width, height):
        '''
            method constructor
            Args:
                width: width of the rectangle
                height: height of the rectangle
        '''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        super().__init__()
        self.__width = width
        self.__height = height
