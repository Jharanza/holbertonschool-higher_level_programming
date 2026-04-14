#!/usr/bin/python3
''' Prints all integers of a list in reverse order '''

def print_reversed_list_integer(my_list=[]):
    for x in range(len(my_list), 0, -1):
        print('{}'.format(my_list[x - 1]))
