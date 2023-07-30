#!/usr/bin/python3
''' Method 10-square that inherits form Rectangle '''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    ''' class Square that inherits from Rectangle '''
    def __init__(self, size):
        '''
            method Constructor
            Args:
                size: The size of the rectangle
        '''
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        ''' Method area that returns the square '''
        return self.__size * self.__size
