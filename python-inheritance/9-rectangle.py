#!/usr/bin/python3
'''
    Module 9-rectangle
'''


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    ''' class Rectangle that inherits methods of BaseGeometry '''
    def __init__(self, width, height):
        '''
            Method constructor that validate width and height
            Args:
                width: The width of the rectangle
                height: The height of the rectangle
        '''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        super().__init__()
        self.__width = width
        self.__height = height

    def area(self):
        ''' method that returns the area of the rectangle'''
        return self.__width * self.__height

    def __str__(self):
        ''' method that return the rep of the rectangle '''
        text = "[Rectangle] {} {}"
        return text.format(self.__width, self.__height)
