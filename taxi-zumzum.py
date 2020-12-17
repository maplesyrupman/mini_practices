#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 16:33:47 2020

@author: max
"""

def taxi_zum_zum(moves):
    x=0
    y=0
    direction= 1
    for i in range(len(moves)):
        if moves[i] == 'F':
            if direction == 1:
                y+= 1
            if direction == 2:
                x+= 1
            if direction == 3:
                y-= 1
            if direction == 4:
                x-= 1
        if moves[i] == 'R':
            direction+= 1
            if direction == 5:
                direction = 1
        if moves[i] == 'L':
            direction-= 1
            if direction == 0:
                direction = 4
    return(x,y) 


