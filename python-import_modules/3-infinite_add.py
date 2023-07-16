#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    suma = 0
    for i in range(len(sys.argv)):
        if i > 0:
            suma = suma + int(sys.argv[i])
    print(f"{suma}")
