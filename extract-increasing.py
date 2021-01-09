#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 18:09:59 2020

@author: max
"""

def extract_increasing(digits):
    last = None
    current = ''
    nlist = []
    for d in digits: 
        
        if last == None:
            last = int(d) 
            nlist.append(last)
            continue
        
        current += d 
        if int(current) > last:
            last = int(current)
            nlist.append(last)
            current = ''
            
    return nlist