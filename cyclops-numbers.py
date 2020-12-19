#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 17:38:17 2020

@author: max
"""

def is_cyclops(n):
    nstring= str(n)
    mid= len(nstring)//2
    if len(nstring)== 1 and nstring[0] == '0':
        return True
    for f in nstring[:mid:-1]:
        if f == '0':
            return False
    for b in nstring[mid+1:]:
        if b == '0':
            return False
    return True
        
                 
 
print(is_cyclops(123404321))
print(is_cyclops(123404301))
print(is_cyclops(0))
