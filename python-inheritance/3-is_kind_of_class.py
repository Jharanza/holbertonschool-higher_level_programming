#!/usr/bin/python3
'''
    module 3-is_kind_of_class
'''


def is_kind_of_class(obj, a_class):
    '''
        method that return True or False if an object is a instance
        of a class or a sub-class
        Args:
            obj: Object to be checked
            a_class: Class to be checked
    '''
    return isinstance(obj, a_class)
