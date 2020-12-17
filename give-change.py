#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 17:00:35 2020

@author: max
"""

def give_change(amount, coins):
    change= []
    for coin in coins:
        for i in range(amount//coin):
            change.append(coin) 
        amount -= (amount//coin)*coin 
    return change 

