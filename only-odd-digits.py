#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 15:48:30 2020

@author: max
"""

def only_odd_digits(n):
    if n<10 and n%2 == 0:
        return False
    if n<10 and n%2 != 0:
        return True
    d= n%10
    if d%2==0:
        return False
    return only_odd_digits(n//10) 
    
n1= 135792
n2= 1357

print(only_odd_digits(n2))

            
    