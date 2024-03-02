#!/usr/bin/python3
'''  '''

def add_tuple(tuple_a=(), tuple_b=()):
    a = list(tuple_a)
    b = list(tuple_b)
    
    if len(a) < 2:
        while len(a) < 2:
            a.append(0)
            
    if len(b) < 2:
        while len(b) < 2:
            b.append(0)

    c = []
    for i in range(2):
        c.append(a[i] + b[i])
        
    return tuple(c)
