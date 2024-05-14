#!/usr/bin/python3
"""Create a singly linked list"""

class Node:
    """Creation of the class Node"""

    def __init__(self, data, next_node=None):
        """Contructor"""
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """Getter return the instance with the value already assigned"""
        return self.__data

    @data.setter
    def data(self, value):
        """Setter validate type of value and assign value to instance __data"""
        if type(value) != int:
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        """Getter return the instance with the value already assigned"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Setter validate type of value and assign value to instance __next_node"""
        if not isinstance(value, Node):
            raise TypeError('next_node must be a Node object')
        self.__next_node = value


class SinglyLinkedList:
    """Define a class single linked list"""
    
    def __init__(self):
        """Constructor"""
        self.__head = None


    def sorted_insert(self, value):
        """Insert a new node """
        new_node = Node(value)
        if self.__head is None or self.__head.data >= value:
            new_node.__next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.__next_node is not None and current.__next_node.data < value:
                current = current.__next_node
            new_node.__next_node = current.__next_node
            current.__next_node = new_node

    def __str__(self):
        """Print the single linked list"""
        if self.__head is None:
            return 'SinglyLinkedList is empty'

        result = ''
        current = self.__head

        while current is not None:
            result += str(current.data) + '\n'
            current = current.__next_node

        return result
