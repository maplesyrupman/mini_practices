#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 18:31:50 2021

@author: max
"""

def safe_squares_rooks(n, rooks):
    x = [True for i in range(n)]
    y = [True for i in range(n)]
    
    for rook in rooks:
        x[rook[0]] = False
        y[rook[1]] = False
        
    xx = 0
    yy = 0
    for xSquare in x:
        if xSquare == True:
            xx += 1
    for ySquare in y:
        if ySquare == True:
            yy += 1
        
    return xx * yy



