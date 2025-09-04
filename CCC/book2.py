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
            for a in wordLis:
                if flag:
                    break
                for b in a:
                    if flag:
                        break
                    for c in b:
                        if c == message[i]:
                            cnt += 1
                        if cnt == desiredIndex:
                            print(f"a {a}")
                            print(f"b {b}")
                            print(f"c {c}")
                            print("--------------------")
                            sentence = wordLis.index(a)+1
                            print(sentence)
                            word = wordLis[sentence-1].index(b)+1
                            print(word)
                            character = wordLis[sentence-1][word-1].index(c)+1
                            print(character)

                            s+=str(sentence) + "." + str(word) + "." + str(character) + "\n"
                            flag = True
                            break
        else:
            s += message[i]
    print(s)
    return s

encodeMessage("ACSL, or the American Computer Science League, is an international computer science competition among more than 300 schools.  Originally founded in 1978 as the Rhode Island Computer Science League, it then became the New England Computer Science League.","American Computer Science League (ACSL) is fun!")
