#!/usr/bin/python3
""" Create a Square class with a method to print the square"""

class Square:
    
    def __init__(self, size=0, position=(0,0)) -> None:
        """ Constructor """
        self.size = size
        self.position = position

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
        
    @property
    def position(self): 
        """ Getter """   
        return self.__position
    
    @position.setter
    def position(self, value):
        """ Setter """
        if type(value) != tuple or len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self) -> int:
        """ Returns the square area """
        return self.__size * self.__size

    def my_print(self):
        """ Print the square """
        if self.size == 0:
            print()
            return
        
        x, y = self.position
        
        for _ in range(y):
            print()
            
        for _ in range(self.size):
            print(' ' * x + '#' * self.size)