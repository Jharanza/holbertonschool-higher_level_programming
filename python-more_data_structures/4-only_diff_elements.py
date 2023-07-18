#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    in_set_1 = set_1.difference(set_2)
    in_set_2 = set_2.difference(set_1)
    result = in_set_1.union(in_set_2)
    return result
