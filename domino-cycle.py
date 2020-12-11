#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 12:16:28 2020

@author: max
"""

def domino_cycle(tiles):
    for i in range(len(tiles)):
        if tiles[i][0] != tiles[i-1][1]:
            return False
    return True 

