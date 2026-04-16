#!/usr/bin/python3
"""Module that defines a Rectangle class with a deletion message."""


class Rectangle:
    """Represents a rectangle that prints a message when deleted."""

    def __init__(self, width=0, height=0):
        """Initialize a Rectangle instance.

        Args:
            width (int): The width of the rectangle. Defaults to 0.
            height (int): The height of the rectangle. Defaults to 0.
        """
        self.__width = None
        self.__height = None
        self.width = width
        self.height = height

    @property
    def width(self):
        """int: The width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """int: The height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of the rectangle, or 0 if width or height is 0."""
        if self.width == 0 or self.height == 0:
            return 0
        return self.width * 2 + self.height * 2

    def __str__(self):
        """Return a string representation of the rectangle using '#' characters."""
        if self.width == 0 or self.height == 0:
            return ''

        rect_str = ''
        for x in range(self.height):
            for _ in range(self.width):
                rect_str += '#'
            if x < self.height - 1:
                rect_str += '\n'

        return rect_str

    def __repr__(self):
        """Return a string that can recreate the rectangle instance."""
        return f"{self.__class__.__name__}({self.width}, {self.height})"

    def __del__(self):
        """Print a farewell message when the rectangle is deleted."""
        print('Bye rectangle...')
