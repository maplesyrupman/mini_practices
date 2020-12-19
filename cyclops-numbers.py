#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 17:38:17 2020

@author: max
"""

def is_cyclops(n):
    nstring= str(n)
    if len(nstring)%2==0:
        return False
    mid = len(nstring)//2
    if nstring[mid] != '0':
        return False
    for f in nstring[:mid:-1]:
        if f == '0':
            return False
    for i in range(len(nstring[mid:])):
        if len(nstring) > 2 and nstring[i-1] == '0':
            return 
    return True
        
                 
 
print(is_cyclops(123404321))
print(is_cyclops(123404301))
print(is_cyclops(0))