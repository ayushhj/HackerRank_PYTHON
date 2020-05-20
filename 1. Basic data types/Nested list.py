lst = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    name = str(input())
    score = float(input())
    lst2= [name,score]
lst.append(lst2)
print(lst)
