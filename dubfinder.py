#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 22:48:02 2020

@author: max
"""

def dubfind(a_list):
    compstart=1
    for i in a_list:
        comps= a_list[compstart:]
        for c in comps:
            print(i,c)
            if c == i:
                return True
        compstart+=1
        print('__')
    return False

list_a= [n for n in range(10)]
#list_a.append(1)
print(list_a)

print(dubfind(list_a)) 