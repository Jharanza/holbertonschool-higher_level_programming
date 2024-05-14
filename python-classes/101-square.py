#!/usr/bin/python3
""" Create a Square class with a method to print the square"""

class Square:

    def __init__(self, size=0, position=(0,0)) -> None:
        """ Constructor """
        self.__size = size
        self.__position = position

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
        if not isinstance(value, tuple) or len(value) != 2 or type(value[0]) != int or type(value[1]) != int:
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

        x, y = self.__position

        for _ in range(y):
            print()

        for _ in range(self.__size):
            print(' ' * x + '#' * self.__size)

    def __str__(self):
        """Print the square"""
        result = ''
        if self.__size == 0:
            result += '\n'
        else:
            for _ in range(self.__position[1]):
                result += '\n'
            for _ in range(self.__size):
                result += ' ' * self.__position[0] + '#' * self.__size + '\n'
        return result
