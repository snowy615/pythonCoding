#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'encodeMessage' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING text
#  2. STRING message
#

def encodeMessage(text, message):
    sentenceLis = text.replace('!', '.').replace('?', '.').split('.  ')
    wordLis = []
    for i in range(len(sentenceLis)):
        wordLis.append(sentenceLis[i].split())
    print(wordLis)

    #message encryption
    s = ""
    messageLength = len(message)
    for i in range(messageLength):
        if message[i] == ' ':
            s += "_"
        elif 122 >= ord(message[i]) >= 97 or 65 <= ord(message[i]) <= 90:
            desiredIndex = i+1
            while True:
                if desiredIndex <= text.count(message[i]):
                    break
                desiredIndex //= 2
            cnt = 0
            flag = False
            for a in range(len(wordLis)):
                if flag:
                    break
                alen = len(wordLis[a])
                for b in range(alen):
                    if flag:
                        break
                    blen = len(wordLis[a][b])
                    for c in range(blen):
                        if wordLis[a][b][c] == message[i]:
                            cnt += 1
                        if cnt == desiredIndex:
                            s+=str(a+1) + "." + str(b+1) + "." + str(c+1) + "\n"
                            flag = True
                            break
        else:
            s += message[i]
    print(s)
    return s

encodeMessage("ACSL, or the American Computer Science League, is an international computer science competition among more than 300 schools.  Originally founded in 1978 as the Rhode Island Computer Science League, it then became the New England Computer Science League.","American Computer Science League (ACSL) is fun!")
