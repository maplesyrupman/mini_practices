#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 15:03:46 2020

@author: max
"""

def count_dominators(items):
    count= 0 
    highest= None
    for i in items[::-1]:
        if highest== None or i > highest:
            count+= 1
            highest= i
    return count 

