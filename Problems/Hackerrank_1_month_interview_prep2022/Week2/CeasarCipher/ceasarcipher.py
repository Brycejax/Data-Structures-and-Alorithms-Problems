#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    # Write your code here
    string = ""
    for i in s:
        i = ord(i)
        if 65 <= i <= 90:
            i = (65 + (i - 65 + k) % 26)
        elif 97 <= i <= 122:
            i = (97 + (i - 97 + k) % 26)
        i = chr(i)
        string += i
        
    return string
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
