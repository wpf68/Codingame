# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    PlayingCardOdds.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pwolff <pwolff@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/11/11 17:29:54 by pwolff            #+#    #+#              #
#    Updated: 2024/11/11 17:30:29 by pwolff           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


listCard = "23456789TJQKA"
compteDeled = 0
compteSearch = 0
lenDeck = 52


def createdDeck ():
    deck = []


    for color in "CDHS":
        for card in listCard:
            deck.append(card[0]+color)


    return deck

def testDeck(deck):
    test = ""
    for card in deck:
        color = card[1]
        if test != card[1]:
            print("\n", file=sys.stderr, flush=True)
            
        print(card + " ", end='', file=sys.stderr, flush=True)
        test = color
    print("\n", file=sys.stderr, flush=True)


deck = createdDeck()
testDeck(deck)

# print("Deck :\n", deck, file=sys.stderr, flush=True)


def typeClean(removed):
    delClean = []
    i = 0
    while i < len(removed):
        if removed[i] in listCard:
            if i + 1 < len(removed) and removed[i + 1] in "CDHS":
                delClean.append(removed[i:i+2])
                i += 1
                # continue
            else:
                delClean.append(removed[i])
        elif removed[i] in "CDHS":
            delClean.append(removed[i])
        i += 1


    return delClean


def cleanFourCard(deck, clean, compteDeled):
    for color in "CDHS":
        try:
            deck.remove(clean + color)
            compteDeled += 1
        except :
            print("** Except **", file=sys.stderr, flush=True)

    return deck, compteDeled


def cleanColor(deck, color, compteDeled):

    for value in listCard:
        try:
            deck.remove(value + color)
            compteDeled += 1
        except :
            print("** Except **", file=sys.stderr, flush=True)

    return deck, compteDeled


def cleanDeck(deck, removed, compteDeled):

    delClean = typeClean(removed)
    print("delClean : ", delClean, file=sys.stderr, flush=True)

    for clean in delClean:
        if clean in listCard:
            deck, compteDeled = cleanFourCard(deck, clean, compteDeled)
        elif clean in "CDHS":
            deck, compteDeled = cleanColor(deck, clean, compteDeled)
        else:
            try:
                deck.remove(clean)
                compteDeled += 1
            except :
                print("** Except **", file=sys.stderr, flush=True)



    return deck, compteDeled
    

def searchDeck(deck, sought,compteSearch):

    listSearch = typeClean(sought)
    print("search : ", listSearch, file=sys.stderr, flush=True)

    for clean in listSearch:
        if clean in listCard:
            deck, compteSearch = cleanFourCard(deck, clean, compteSearch)
        elif clean in "CDHS":
            deck, compteSearch = cleanColor(deck, clean, compteSearch)
        else:
            try:
                deck.remove(clean)
                compteSearch += 1
            except :
                print("** Except **", file=sys.stderr, flush=True)



    return deck, compteSearch








r, s = [int(i) for i in input().split()]
for i in range(r):
    removed = input()
    print("Remove :", removed, file=sys.stderr, flush=True)
    deck, compteDeled = cleanDeck(deck, removed, compteDeled)
    testDeck(deck)
    lenDeck = len(deck)
    
for i in range(s):
    sought = input()
    print("Sought :", sought, file=sys.stderr, flush=True)
    deck, compteSearch = searchDeck(deck, sought, compteSearch)

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)



testDeck(deck)
print("Nombre de cartes deled : ", compteDeled, " len de deck ", lenDeck, file=sys.stderr, flush=True)
print("Nombre de cartes a chercher : ", compteSearch, " len de nouveau deck ", len(deck), file=sys.stderr, flush=True)

if lenDeck != 0:
    resultat = round(compteSearch / lenDeck * 100)
    print(str(resultat) + "%")
else:
    print("40%")
