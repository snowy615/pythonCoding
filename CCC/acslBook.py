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
    s = ""

    #establish code for encryption
    punctuationLis = []
    for i in range(len(text)):
        if text[i] == '.' or text[i] == '?' or text[i] == '!':
            punctuationLis.append(i)
    print(punctuationLis)

    #message encryption
    messageLength = len(message)
    for i in range(messageLength):
        letter = message[i]
        number = ord(letter)
        print(f"letter {letter} number {number}")
        if letter == ' ':
            s += "_"
            print("blank")
        elif 122>=number>=97 or 65<=number<=90:
            occurence = text.count(letter)
            print(f"oc{occurence}")
            desiredIndex = i+1
            while desiredIndex >= occurence:
                desiredIndex = int(desiredIndex/2)
                print("while")
            print(f"desiredIndex {desiredIndex}")
            cnt = 0
            for j in range(len(text)):
                if text[j] == letter:
                    cnt += 1

                if cnt == desiredIndex:
                    # look for sentence, word, character
                    sentence = 0
                    word = 0
                    character = 0
                    #find
                    while True:
                        if j <= punctuationLis[sentence] and sentence<len(punctuationLis)-1:
                            break
                        sentence += 1
                        print(j, sentence)
                    sentence += 1
                    print(f"sentence {sentence}")


                    s += str(sentence) + "." + str(word) + "." + str(character) + "\n"
                    break

        else:
            s += letter
        print("----------------")

    print(f"s {s}")
    return s

encodeMessage("ACSL, or the American Computer Science League, is an international computer science competition among more than 300 schools.  Originally founded in 1978 as the Rhode Island Computer Science League, it then became the New England Computer Science League.","American Computer Science League (ACSL) is fun!")

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    text = input()

    message = input()

    result = encodeMessage(text, message)

    fptr.write(result + '\n')

    fptr.close()
