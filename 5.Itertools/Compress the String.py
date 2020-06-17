from itertools import groupby

for key, group in groupby(input()): 
    key= int(key)
    count = len(list(group))
    print((count,key),end=" ")
