#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 16:28:56 2020

@author: max
"""

def letters_in_words(words, letters):
    word_list= []
    for word in words:
        if letters in word:
            word_list.append(word)
    return word_list 

somewords= ['book', 'shook', 'look', 'hook', 'took', 'hello', 'cat', 'dog', 'too']

print(letters_in_words(somewords, 'oo'))