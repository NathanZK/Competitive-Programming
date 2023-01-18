#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    swaps = 0
    size = len(a)
    for i in range(size):
        for j in range(size -1 - i):
            if a[j] > a[j + 1]:
                a[j + 1], a[j] = a[j], a[j + 1]
                swaps += 1
    print("Array is sorted in {} swaps.".format(swaps))
    print("First Element:", a[0])
    print("Last Element:", a[-1])

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
