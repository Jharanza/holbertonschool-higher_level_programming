#!/usr/bin/python3
'''
    : Multiply all number of a list without loops
    : my_list: list of numbers to multiply
    : number: Value to multiply all the numbers in the list
    : Return: The result of the multiply
'''
def multiply_list_map(my_list=[], number=0):
    return list(map(lambda x: x * number, my_list))
