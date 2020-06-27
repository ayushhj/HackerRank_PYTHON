from itertools import product
n,m=map(int, input().split())
l1=list()
for i in range(n):
    l=list(map(int,input().split()))[1:]
    l1.append(l)
r=map(lambda x:sum(i*i for i in x)%m,product(*l1))    
print(max(r))