#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 17:38:17 2020

@author: max
"""

def is_cyclops(n):
    sn= str(n)
    mid= len(sn)//2
    if len(sn)%2==0:
        return False
    if sn[mid] == '0':
        for f in sn[:mid]:
            if f == '0':
                return False
        for b in sn[mid+1:]:
            if b == '0':
                return False
    return True 
     
 
print(is_cyclops(123404321))
print(is_cyclops(123404301))
print(is_cyclops(0))