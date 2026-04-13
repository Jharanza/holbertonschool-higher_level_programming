#!/usr/bin/python3
''' Print the numbers from 0 to 99 '''

for x in range(100):
  if x < 99:
    print('{}, '.format(str(x).rjust(2, '0')), end='')
  else:
    print(x)
