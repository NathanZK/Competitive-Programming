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

def insertionSort1(n, arr):
    # Write your code here
    val = arr[n - 1]
    i = n - 2
    while i >= 0 and val < arr[i]:
        arr[i+1] = arr[i]
        i -= 1
        printList(arr)
    arr[i+1] = val
    printList(arr)
    
def printList (arr):
    for i in arr:
        print(i, end = " ")
    print()

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
