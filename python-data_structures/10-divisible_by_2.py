#!/usr/bin/python3
''' Finds all multiples of 2 in a list. '''

def divisible_by_2(my_list=[]):
    new_list = []

    for x in my_list:
        new_list.append(x % 2 == 0)

    return new_list
