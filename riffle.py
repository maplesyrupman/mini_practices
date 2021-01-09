#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 21:00:35 2020

@author: max
"""

def riffle(items, out=True):
    shfl_items= []
    
    if items:
        mid= len(items)//2
        left= items[:mid]
        right= items[mid:]
        
        while left or right:
            if out:
                shfl_items.append(left.pop(0))
                shfl_items.append(right.pop(0))
            else:
                shfl_items.append(right.pop(0))
                shfl_items.append(left.pop(0))
                
    return shfl_items 

items= [i for i in range(10)]

print(items)
print(riffle(items)) 
