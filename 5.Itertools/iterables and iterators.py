from itertools import combinations;
l = int(input())
s = input().split()
k = int(input())

count = 0
total =0
for i in combinations(s,k):
    total=total+1
    if 'a' in i:
        count=count+1
probab= (count / total)
print("%.4f"%probab) 