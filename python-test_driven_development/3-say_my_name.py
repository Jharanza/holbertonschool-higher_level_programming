#!/usr/bin/python3
'''
    Module 3-say_my_name returns a string
'''


def say_my_name(first_name, last_name=""):
    '''
        Function print the name and lasts name
        Args:
            first_name: 1st string argument rep first name
            last_name: 2nd string argument rep last name
            return. nothing
    '''
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))
