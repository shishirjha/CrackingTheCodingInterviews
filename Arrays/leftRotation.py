# Link for the problem
# https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
# def rotSingleLeft(a):
#     temp = a[0]
#     for i in range(1,len(a)):
#         a[i-1] = a[i]
#     a[-1] = temp

def rotLeft(a, d):
    new_a = [0]*len(a)
    for i in range(len(a)-1,-1,-1):
        new_index = i-d
        new_a[new_index] = a[i]
    return new_a
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
