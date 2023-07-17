#!/usr/bin/python3
def common_elements(set_1, set_2):
    new_set = set()
    for A in set_1:
        for B in set_2:
            if A == B:
                new_set.add(A)
    return new_set
