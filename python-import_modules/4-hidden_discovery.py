#!/usr/bin/python3
if __name__ == "__main__":
    import sys as s
    import hidden_4

    names = dir(hidden_4)

    i = 0
    for name in names:
        if name[0] != '_':
            print(name)
