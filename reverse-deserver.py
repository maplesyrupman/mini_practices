#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 20:52:02 2020

@author: max
"""

def reverse_reversed(items):
    new_list= []
    for i in items[::-1]:
        if type(i) is list:
            new_list.append(reverse_reversed(i))
        else:
            new_list.append(i) 
        
    return new_list 

