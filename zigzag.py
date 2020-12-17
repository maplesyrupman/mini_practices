#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 22:20:05 2020

@author: max
"""

def is_zigzag(n):
    nstring= str(n) 
    plusminus= None
    plusminuslast= None
    lastidx= 0
    
    for i in range(1,len(nstring)):
        if nstring[lastidx] > nstring[i]:
            plusminus= -1
        if nstring[lastidx] < nstring[i]:
            plusminus= 1
        if plusminus == plusminuslast:
            return False
        plusminuslast= plusminus 
        lastidx+=1
        
    return True

print(is_zigzag(15391))
print(is_zigzag(16321))