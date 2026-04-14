#!/usr/bin/python3
from sys import argv

sum = 0
for elem in argv[1:]:
  sum += int(elem)

if __name__ == '__main__':
  print(sum)
