a=int(input())
M=set(int(i) for i in input().split(" "))
b=int(input())
N=set(int(i) for i in input().split(" "))
u= M.union(N)
intersc= M.intersection(N)
symmetric_diff = u-intersc
L = list(symmetric_diff)
L.sort()
for i in L:
    print(i)