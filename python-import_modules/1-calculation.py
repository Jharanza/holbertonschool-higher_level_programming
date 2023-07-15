#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import calculator_1 as cls
    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, cls.add(a, b)))
    print("{} - {} = {}".format(a, b, cls.sub(a, b)))
    print("{} * {} = {}".format(a, b, cls.mul(a, b)))
    print("{} / {} = {}".format(a, b, cls.div(a, b)))
