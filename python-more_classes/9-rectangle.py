#!/usr/bin/python3
"""Module that defines a Rectangle class with a square factory method."""


class Rectangle:
    """Represents a rectangle with comparison and square creation capabilities."""

    number_of_instances = 0
    """int: Counts the current number of Rectangle instances."""

    print_symbol = '#'
    """any: Symbol used to draw the rectangle in string representation."""

    def __init__(self, width=0, height=0):
        """Initialize a Rectangle instance and increment the instance counter.

        Args:
            width (int): The width of the rectangle. Defaults to 0.
            height (int): The height of the rectangle. Defaults to 0.
        """
        self.__width = None
        self.__height = None
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        """Return a string representation of the rectangle using print_symbol."""
        if self.width == 0 or self.height == 0:
            return ''

        return '\n'.join(str(self.print_symbol) * self.width for _ in range(self.height))

    def __repr__(self):
        """Return a string that can recreate the rectangle instance."""
        return f"{self.__class__.__name__}({self.width}, {self.height})"

    def __del__(self):
        """Decrement the instance counter and print a farewell message."""
        Rectangle.number_of_instances -= 1
        print('Bye rectangle...')

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the rectangle with the greater or equal area.

        Args:
            rect_1 (Rectangle): The first rectangle.
            rect_2 (Rectangle): The second rectangle.

        Returns:
            Rectangle: rect_1 if its area is greater or equal, otherwise rect_2.

        Raises:
            TypeError: If rect_1 or rect_2 is not a Rectangle instance.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError('ect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('ect_1 must be an instance of Rectangle')

        if rect_1.area() < rect_2.area():
            return rect_2

        return rect_1

    @classmethod
    def square(cls, size=0):
        """Return a new Rectangle instance with equal width and height.

        Args:
            size (int): The side length of the square. Defaults to 0.

        Returns:
            Rectangle: A new Rectangle where width == height == size.
        """
        return cls(size, size)
