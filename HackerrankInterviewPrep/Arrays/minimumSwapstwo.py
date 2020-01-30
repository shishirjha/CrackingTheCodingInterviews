# Link to the problem
# https://www.hackerrank.com/challenges/minimum-swaps-2/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    temp = {a: i for i, a in enumerate(arr)}
    swaps = 0
    for i in range(len(arr)):
        actual, expected = arr[i], i + 1
        actual_i, expected_i = i, temp[expected]
        if actual != expected:
            arr[actual_i] = expected
            arr[expected_i] = actual
            temp[actual] = expected_i
            temp[expected] = actual_i
            swaps += 1
    return swaps




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
