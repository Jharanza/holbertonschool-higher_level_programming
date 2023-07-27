#!/usr/bin/python3
'''
    module 0-lookup
'''

class My_class:
    ''' My class returns methods and attributes of an object'''

    def lookup(obj):
        '''
            lookup: This method returns the available methods and attributes
            of an object.
            Args:
                obj: Only argumento to check
        '''
        return dir(obj)
