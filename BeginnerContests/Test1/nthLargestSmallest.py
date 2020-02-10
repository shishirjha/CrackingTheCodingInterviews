# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())
for i in range(T):
    m,n = list(map(int, input().split()))
    l = list(map(int, input().split()))
    l.sort()
    maximum = l[-1]
    minimum = l[0]
    smallCount=0
    largeCount=0
    thirdSmallest=minimum
    thirdLargest=maximum
    for i in range(len(l)):
        if l[i] > minimum and smallCount != (n-1):
            thirdSmallest = l[i]
            smallCount+=1
    for i in range(len(l)-1,-1,-1):
        if l[i]< maximum and largeCount != (n-1):
            thirdLargest=l[i]
            largeCount+=1
    print('{} {}'.format(thirdSmallest, thirdLargest))