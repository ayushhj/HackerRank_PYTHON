from collections import defaultdict
n,m= map(int,input().split())
lis=[]
d=defaultdict(list)
for i in range(n):
    x=input()
    d[x].append(i+1)
for i in range(m):
    y=input()
    lis.append(y)
for i in lis:
    if i in d:
        print(' '.join(map(str,d[i])))
    else:
        print(-1)