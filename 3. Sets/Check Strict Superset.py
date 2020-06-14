a = set(map(int, input().split()))
n= int(input())
for i in range(n):
    b = set(map(int, input().split()))
    if a.issuperset(b) != True or len(a) == len(b): 
        print(False)
        break
else: print(True)
