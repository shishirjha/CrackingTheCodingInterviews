# Link for the problem
# https://www.hackerrank.com/challenges/new-year-chaos/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    moves = 0
    for i in range(len(q)):
        if q[i]-i > 3:
            print("Too chaotic")
            return
        for j in range(max(q[i]-2,0),i):
            if q[j]>q[i]:
                moves+=1
    print(moves)

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)


        