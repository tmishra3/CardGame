#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 04:19:01 2018

@author: tanmay
"""
#21 CARDS TRICK

from CardDeck import card, deck
import sys
from termcolor import colored, cprint

for i in range(0,30):
    print("\n")
print("-----------------21 CARD TRICK!-----------------\n")
#Code above inserts 30 lines of blank space and then prints out the game
#name.

mainDeck = deck("MAIN DECK") #Creates the main deck of 52 cards.

for i in range(0,10):
    mainDeck.shuffleDeck() #Shuffles the deck 10 times.

DecksOf7 = [deck("1ST DECK OF 7",False),deck("2ND DECK OF 7",False),deck("3RD DECK OF 7",False)]

#The above code makes 3 empty decks. The parameter "false" means it's a "false"
#deck (aka, empty). This is an optional parameter. The first parameter is
#the name of the deck.

for i in range(0,7):
    DecksOf7[0].addCard(mainDeck.removeRandCard())
    DecksOf7[1].addCard(mainDeck.removeRandCard())
    DecksOf7[2].addCard(mainDeck.removeRandCard())

#The above code within the for loop is going to randomly pick
#a card and add to it to each Deck of 7 for a total of 7 cards
#per deck. Obviously, the main deck will then have 52 - 21 cards
#or 31 cards left in it since we're removing the cards from the
#main deck itself.

for i in range (0,3):
    DecksOf7[i].printDeck()
#Display the name of the deck along with the cards in those decks.

print(colored("You have 3 decks of cards. Pick a card from a deck and remember it.", 'blue', attrs=['bold']))
print(colored("Which deck was your card in, (1,2 or 3) ? ", 'blue', attrs=['bold']))
firstRound = input('')
print("\n")

firstPick = deck("FIRST PICK",False)

firstRound = str(firstRound)

if (firstRound=="1"):
    orderShuffle = [1,0,2]
if (firstRound=="2"):
    orderShuffle = [0,1,2]
if (firstRound=="3"):
    orderShuffle = [0,2,1]
    
for i in range (0,3):
    for j in range(0,7):
        firstPick.addCard(DecksOf7[orderShuffle[i]].returnCardN(j+1),1)

for i in range (0,3):
    DecksOf7[i].emptyDeck()
    

counter = 0
for j in range (0,7):
    for i in range(0,3):
        DecksOf7[2-i].addCard(firstPick.returnCardN(1+counter))
        counter += 1

for i in range (0,3):
    DecksOf7[i].printDeck()

print(colored("Which deck is your card in (1,2 or 3)? ", 'blue', attrs=['bold']))
firstRound = input('')
print("\n")

firstRound = str(firstRound)

if (firstRound=="1"):
    orderShuffle = [1,0,2]
if (firstRound=="2"):
    orderShuffle = [0,1,2]
if (firstRound=="3"):
    orderShuffle = [0,2,1]

firstPick.emptyDeck()
    
for i in range (0,3):
    for j in range(0,7):
        firstPick.addCard(DecksOf7[orderShuffle[i]].returnCardN(j+1))

for i in range (0,3):
    DecksOf7[i].emptyDeck()
    

counter = 0
for j in range (0,7):
    for i in range(0,3):
        DecksOf7[2-i].addCard(firstPick.returnCardN(1+counter))
        counter += 1
        
for i in range (0,3):
    DecksOf7[i].printDeck()

print(colored("One last time, Which deck is your card in (1,2 or 3)? ", 'blue', attrs=['bold']))
firstRound = input('')
print("\n")

firstRound = str(firstRound)

if (firstRound=="1"):
    orderShuffle = [1,0,2]
if (firstRound=="2"):
    orderShuffle = [0,1,2]
if (firstRound=="3"):
    orderShuffle = [0,2,1]  

firstPick.emptyDeck()
    
for i in range (0,3):
    for j in range(0,7):
        firstPick.addCard(DecksOf7[orderShuffle[i]].returnCardN(j+1))

for i in range (0,3):
    DecksOf7[i].emptyDeck()
    

counter = 0
for j in range (0,7):
    for i in range(0,3):
        DecksOf7[2-i].addCard(firstPick.returnCardN(1+counter))
        counter += 1

print(colored("\nLet me guess...your card is " + str(DecksOf7[1].returnCardN(4)) + " ?", 'blue', attrs=['bold']))
