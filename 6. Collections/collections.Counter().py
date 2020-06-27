from collections import Counter
x = input()
shoes = Counter(list(map(int, input().split())))
c=list(shoes.elements())
N = int(input())
money= 0
for l in range(N):
    size ,price = input().split()
    size = int(size)
    price = int(price)
    if size in c:
        c.remove(size)
        money = money + price
print(money)