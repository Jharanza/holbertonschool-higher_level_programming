#!/usr/bin/python3


def add_attribute(obj, att_name, att_val):

  if hasattr(obj, "__dict__"):
    setattr(obj, att_name, att_val)
  else:
    raise TypeError("can't add new attribute")
