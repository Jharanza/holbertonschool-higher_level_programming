#!/usr/bin/python3
'''
    module 1-my_list
'''


class MyList(list):
    ''' class to sort a list '''

    def print_sorted(self):
        ''' method that sort a list in ascendent form '''
        print(sorted(self))
