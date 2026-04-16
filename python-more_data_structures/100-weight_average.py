#!/usr/bin/python3

def weight_average(my_list=[]):
  if len(my_list) == 0:
    return 0

  weight = 0
  people = 0
  for e in my_list:
    weight += e[0] * e[1]
    people += e[1]

  return weight / people
