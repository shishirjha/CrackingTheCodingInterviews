# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())
for i in range(T):
    l = list(map(int, input().split()))
    ans = (((l[0]+l[1])*l[2])//l[3])-l[4]
    if ans < 0:
        print(-1)
    else:
        print(ans)
    