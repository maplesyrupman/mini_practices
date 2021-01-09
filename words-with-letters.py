#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 16:28:56 2020

@author: max
"""

def words_with_letters(words, letters):
    wordList = []
    for word in words:
        idx=0
        for letter in word:
            if letter == letters[idx]:
                idx+=1
            if (len(letters)) == idx:
                wordList.append(word)
                break
                
    return wordList
        

    


