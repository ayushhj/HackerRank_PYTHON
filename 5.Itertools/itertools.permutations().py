from itertools import permutations

s,k = input().split()
k=int(k)
output = permutations(s,k)

output = sorted(output)

for s in output:
    print(''.join(s))
