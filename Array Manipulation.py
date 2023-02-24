#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def arrayManipulation(n, queries):
    # Write your code here
    nums = {}
    for query in queries:
       nums[query[0]] = nums.get(query[0], 0) + query[2]
       nums[query[1]+1] = nums.get(query[1]+1, 0) - query[2]
    
    prefix = [j for i, j in sorted(nums.items())]
    for i in range(1,len(prefix)):
        prefix[i] += prefix[i-1]
        
    return max(prefix)
        
                
    return max(nums.values())

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
