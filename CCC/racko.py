#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'playRackO' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING info #of slots + # of cards
#  2. STRING rack
#  3. STRING pile
#
def inOrder(hand):
    if hand==sorted(hand):
        return True
    return False
def checkHV(lis):
    hv = 0
    for i in range(len(lis)-1):
        if lis[i+1]<lis[i]:
            hv += 1
    return hv
# return heuristic value + slot
def A(hand, card, handNumber, totalCardNumber):
    cardIndex = hand.index(card)
    ohv = checkHV(hand[max(0, cardIndex-1), min(handNumber, cardIndex+1)])

    hv = -1
    slotIndex = int(totalCardNumber/handNumber)
    if totalCardNumber % handNumber == 0:
        slotIndex -= 1
    if slotIndex*slotIndex<hand[slotIndex]<=slotIndex*(slotIndex+1):
        return hv, slotIndex
    lis = [card]
    if cardIndex != 0:
        lis.insert(0, hand[cardIndex-1])
    if cardIndex != handNumber-1:
        lis.append(hand[cardIndex+1])
    hv = ohv - checkHV(lis)
    return hv, slotIndex

def B(hand, card):
    hv = -1
    slotIndex = -1

    i = 0
    while True:
        if i+2 >= len(hand):
            return hv, slotIndex
        if inOrder(hand[i, i+2])==False:
            if inOrder([card, hand[i+1], hand[i+2]]):
                ohv = checkHV(hand[max(0, i-1), min(len(hand)-1, i+3)])
                lis = [card, hand[i+1], hand[i+2]]
                if i!=0:
                    lis.insert(0, hand[i-1])
                if i+3 <=len(hand)-1:
                    lis.append(hand[i+3])
                hv = ohv-checkHV(lis)
                return hv, i
            if inOrder([hand[i], card, hand[i+2]]):
                ohv = checkHV(hand[max(0, i-1), min(len(hand)-1, i+3)])
                lis = [hand[i], card, hand[i+2]]
                if i!=0:
                    lis.insert(0, hand[i-1])
                if i+3 <=len(hand)-1:
                    lis.append(hand[i+3])
                hv = ohv-checkHV(lis)
                return hv, i+1
            if inOrder([hand[i], hand[i+1], card]):
                ohv = checkHV(hand[max(0, i-1), min(len(hand)-1, i+3)])
                lis = [hand[i], hand[i+1], card]
                if i!=0:
                    lis.insert(0, hand[i-1])
                if i+3 <=len(hand)-1:
                    lis.append(hand[i+3])
                hv = ohv-checkHV(lis)
                return hv, i+2
        i+=1
def playRackO(info, rack, pile):
    handNumber, totalCardNumber = map(int, info.split())
    hand = rack.split()
    draw = pile.split()
    drawIndex = 0
    hv = checkHV(hand)
    while True:
        if drawIndex >= len(draw) or inOrder(hand):
            return str(hand)
        Ahv, AslotIndex = A(hand, draw[drawIndex], handNumber, totalCardNumber)
        Bhv, BslotIndex = B(hand, draw[drawIndex])
        if Ahv == 1 or (Ahv==0 and Bhv!=1):
            # A
            hand[AslotIndex] = draw[drawIndex]
            hv -= Ahv
        elif Bhv != -1:
            # B
            hand[BslotIndex] = draw[drawIndex]
            hv -= Bhv

        drawIndex += 1

playRackO("9 70","40 35 30 56 32 58 44 17 45","31 37 10 28 21 62 7 64 16 12")

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    info = input()

    rack = input()

    pile = input()

    result = playRackO(info, rack, pile)

    fptr.write(result + '\n')

    fptr.close()
