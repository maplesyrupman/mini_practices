#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 15:32:18 2020

@author: max
"""

def is_ascending(items):
    last= items[0]
    for i in items[1:]:
        if i > last:
            last= i
            continue
        return False
    return True