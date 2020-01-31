# Link to the problem
# https://www.hackerrank.com/challenges/ctci-ransom-note/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps

#!/bin/python3
from collections import defaultdict
import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    boolli = False
    d = defaultdict(int)
    for i in magazine:
        d[i]+=1
    for i in note:
        if d[i] == 0:
            boolli = False
            break
        else:
            boolli = True
            d[i]-=1
    # for k,v in d.items():
    #     if k==v:
    #         boolli = True
    #         continue
    #     else:
    #         boolli = False
    #         break
    if boolli == True:
        print("Yes")
    else:
        print("No")
if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)