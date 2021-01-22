#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 17:25:54 2021

@author: max
"""

def before_or_after(current, nxt):
    if current<nxt:
        return 1
    if current == nxt:
        return 0
    if current>nxt: 
        return -1

def words_with_given_shape(words, shape):
    matchingWords = []
    for word in words:
        if len(word) != len(shape) +1:
            continue
        idx=0
        match = True
        for value in shape:
            if value == before_or_after(word[idx], word[idx+1]):
                idx += 1
                continue
            else: 
                match = False
                break
        if match:
            matchingWords.append(word)
            
    return matchingWords
                
            
            
            