n= int(input())
b= set(map(int, input().split()))
max(b)
b.remove(max(b))
print(max(b))