#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 21:07:27 2021

@author: max
"""

def pancake_scramble(text):
    if len(text) < 3:
        result = text[::-1]
        return result 
    
    result = text
    
    flipIdx = 2 #flips first 2 characters first, then first 3 etc..
    while flipIdx <= len(text):
        flipSide = result[:flipIdx]
        staticSide = result[flipIdx:]
        result = flipSide[::-1] + staticSide
        flipIdx += 1 

    return result 

