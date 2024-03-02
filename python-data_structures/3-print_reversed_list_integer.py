#!/usr/bin/python3
''' Prints all integers of a list in reverse order '''

def print_reversed_list_integer(my_list=[]):
    for x in my_list.__reversed__():
        print('{}'.format(x))
