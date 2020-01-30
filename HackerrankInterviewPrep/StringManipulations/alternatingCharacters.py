# https://www.hackerrank.com/challenges/alternating-characters/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    l = list(s)
    val = 0
    for i in range(1,len(l)):
        if l[i] == l[i-1]:
            val+=1
    return val
    # d = {'A':0,'B':0}
    # l = list(s)
    # value = 0
    # for i in s:
    #     if i == 'A':
    #         d['A']+=1
    #     else:
    #         d['B']+=1
    # while d['A']>1:
    #     d['A']-=1
    #     value+=1
    # while d['B']>1:
    #     d['B']-=1
    #     value+=1
    
    # # print(value)
    # return value

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
