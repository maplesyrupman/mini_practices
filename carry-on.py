#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 22:40:55 2020

@author: max
"""

def count_carries(a,b):
    carries=0 
    carried=0
    while a or b:
        lasta= a%10
        lastb= b%10
        if lasta + lastb + carried >=10:
            carries+=1
            carried= 1
        else: 
            carried= 0
        a= a//10 
        b= b//10
        
    return carries 

print(count_carries(3**1000,3**1000+1))