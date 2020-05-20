a=int(input())
s1=set(map(int,input().split()))
N=int(input())

for i in range(N):
    x,y=input().split()
    s2=set(map(int,input().split()))
    if x=='intersection_update':
        s1.intersection_update(s2)
    elif x=='update':
        s1.update(s2)
    elif x=='symmetric_difference_update':
        s1.symmetric_difference_update(s2)
    elif x=='difference_update':
        s1.difference_update(s2)
print(sum(s1))