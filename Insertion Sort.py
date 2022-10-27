#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#
def printList(arr):
    for i in arr:
        print(i, end = " ")
    print()

def insertionSort1(n, arr):
    elem = arr[-1]
    pos = n - 1
    while elem < arr[pos - 1] and pos > 0:
        arr[pos] = arr[pos - 1]
        pos -= 1
        printList(arr)
    arr[pos] = elem
    printList(arr)
 

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
