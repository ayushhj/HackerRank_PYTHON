L = []

N = int(input())

for i in range(N):
    x = input().split()

    if x[0] == 'insert':
        L.insert(int(x[1]), int(x[2]))
    elif x[0] == 'print':
        print(L)
    elif x[0] == 'remove':
        L.remove(int(x[1]))
    elif x[0] == 'append':
        L.append(int(x[1]))
    elif x[0] == 'sort':
        L.sort()
    elif x[0] == 'pop':
        L.pop()
    elif x[0] == 'reverse':
        L.reverse()