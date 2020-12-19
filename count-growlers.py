#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 19:37:05 2020

@author: max
"""

def count_growlers(animals):
    
    Rdog= 0
    Rcat= 0
    Ldog= 0
    Lcat= 0 
    growlers= 0
    
    for animal in animals:
        if Rdog > Rcat and (animal == 'cat' or animal == 'dog'):
            growlers += 1
        if animal == 'dog' or animal == 'god':
            Rdog += 1
        else:
            Rcat += 1
        
    for animal in animals[::-1]:
        if Ldog > Lcat and (animal == 'tac' or animal == 'god'):
            growlers += 1
        if animal == 'dog' or animal == 'god':
            Ldog += 1
        else:
            Lcat += 1
            
    return growlers

print(count_growlers(['dog', 'cat', 'dog', 'god', 'dog', 'god', 'dog', 'god', 'dog', 'dog', 'god', 'god', 'cat', 'dog', 'god', 'cat', 'tac']))