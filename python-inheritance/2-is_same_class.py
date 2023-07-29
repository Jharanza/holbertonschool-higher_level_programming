#!/usr/bin/python3
'''
    module 2-is_same_class
'''


def is_same_class(obj, a_class):
    '''
        Method that return True or false if a object
        es an instance of a class
        Args:
            obj: object to check
            a_class: class to be check
    '''
    return type(obj) is a_class
