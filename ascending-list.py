#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 15:32:18 2020

@author: max
"""

def is_ascending(items):
    if len(items) <= 1:
        return True
    last= items[0]
    for i in items[1:]:
        if i > last:
            last= i
            continue
        return False
    return True

a_list= [1,2,3,4,5,6,7,8,9,10]
another_list= []


print(is_ascending(a_list))
print(is_ascending(another_list))

