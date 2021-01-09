#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 17:38:17 2020

@author: max
"""

def is_cyclops(n):
    nstring= str(n)
    if len(nstring)%2 == 0:
        return False
    mid= len(nstring)//2
    if nstring[mid] == '0':
        if len(nstring) == 1:
            return True
        for f in nstring[:mid]:
            if f == '0':
                return False
        for b in nstring[:mid:-1]:
            if b == '0':
                return False
        return True
    return False
                 
 
