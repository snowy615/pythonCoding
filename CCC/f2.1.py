#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'textingPath' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING names
#  2. STRING start
#

def textingPath(names, start):
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    names = input()

    start = input()

    result = textingPath(names, start)

    fptr.write(result + '\n')

    fptr.close()
