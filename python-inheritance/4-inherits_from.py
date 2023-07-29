#!/usr/bin/python3
'''
    module 4-inherits_from
'''


def inherits_from(obj, a_class):
    '''
        method return True or false if an object is a instance of a class
        and inherited from the class
        Args:
            obj: Object to be checked
            a_class: Class to be checked
    '''
    return issubclass(type(obj), a_class) and type(obj) is not a_class
