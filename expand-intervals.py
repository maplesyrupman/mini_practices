#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 21:03:47 2020

@author: max
"""

def expand_intervals(intervals):
    
    numlist= []
    ints= intervals.split(',') 
    ints2= []
    for i in ints:
        ints2.append(i.split('-'))
    for s in ints2:
        if len(s)==2:
            for r in range(int(s[0]), int(s[1]) +1):
                numlist.append(r)
        if len(s)==1:
            numlist.append(int(s[0]))
            
    return numlist

int1= '1,3-9,12-14,999'

print(expand_intervals(int1))
            
        