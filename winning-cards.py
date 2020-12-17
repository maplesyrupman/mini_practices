#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 18:14:09 2020

@author: max
"""

def winning_card(cards, trump=None):
    rank = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10, 'jack': 11, 'queen': 12, 'king': 13, 'ace': 14} 
    if not trump:
        trump = cards[0][1] 
    winner= cards[0] 
    for card in cards[1:]:
        if card[1] != trump:
            continue 
        elif winner[1] != trump and card[1] == trump:
            winner= card 
            continue 
        if rank[card[0]] > rank[winner[0]]:
            winner= card 
    return winner 

some_cards= [('two', 'clubs'), ('ace', 'diamonds'), ('ace', 'hearts'), ('ace', 'spades')] 

print(winning_card(some_cards))
                
                

        