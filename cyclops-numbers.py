#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 17:38:17 2020

@author: max
"""

def is_cyclops(n):
    nstring= str(n)
    mid= len(nstring)//2
    if nstring[mid] == '0':
        if len(nstring) == 1:
            return True
        for f in nstring[:mid]:
            if f == '0':
                return False
        reverse= [r for r in nstring[::-1]]
        for b in reverse[:mid]:
            if b == '0':
                return False
        return True
    return False
                 
 
print(is_cyclops(12344321))
print(is_cyclops(123404301))
print(is_cyclops(0))
