# Link to the problem
# https://www.hackerrank.com/challenges/frequency-queries/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict as d

# Complete the freqQuery function below.
def freqQuery(queries):
    num = d(int)
    ans=[]
    freq = d(int)
    for q in queries:
        if q[0] == 1:
            freq[num[q[1]]]-=1
            num[q[1]]+=1
            freq[num[q[1]]]+=1
        elif q[0] == 2:
            if num[q[1]]>0:
                freq[num[q[1]]]-=1
                num[q[1]]-=1
                freq[num[q[1]]]+=1
        elif q[0] == 3:
            if freq[q[1]]>0:
                ans.append(1)
            else:
                ans.append(0)
            
    return ans



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
