a=int(input())
M=set(map(int, input().split()))
b=int(input())
N=set(map(int, input().split()))
d=M.difference(N)
print(len(d))
