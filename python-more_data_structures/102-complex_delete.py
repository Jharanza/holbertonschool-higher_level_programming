#!/usr/bin/python3

def complex_delete(a_dictionary, value):
  if value not in a_dictionary.values():
    return a_dictionary

  k_list = []
  for k in a_dictionary.keys():
    if a_dictionary[k] == value:
      k_list.append(k)

  for k in k_list:
    del a_dictionary[k]

  return a_dictionary

  
