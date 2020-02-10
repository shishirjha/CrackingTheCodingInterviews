#!/bin/python3

import os
import sys

def leftRotate(a,n,d):
    auxA=[0]*n
    for i in range(len(a)-1,-1,-1):
        auxA[i-d]=a[i]
    return auxA
if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))
    # print(leftRotate(a,n,d))
    rotatedArray = leftRotate(a,n,d)
    rotatedArray = ' '.join([str(i) for i in rotatedArray])
    print(rotatedArray)