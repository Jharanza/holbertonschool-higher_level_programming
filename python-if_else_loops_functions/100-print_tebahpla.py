#!/usr/bin/python3
''' print the ASCII alphabet in reversed order between lower and uppercase '''

for x in range(122, 96, -1):
  print('{}'.format(chr(x) if x % 2 == 0 else chr(x - 32) ), end='')
