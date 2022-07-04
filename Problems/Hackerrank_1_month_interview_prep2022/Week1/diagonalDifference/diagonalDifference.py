
import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr, n):
    ltr = 0
    rtl = 0
    count1 = 0
    count2 = n - 1
    for i in range(n):
        ltr += arr[i][count1]
        rtl += arr[count2][i]
        count1 += 1
        count2 -= 1
    return abs(ltr - rtl)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr, n)

    fptr.write(str(result) + '\n')

    fptr.close()
