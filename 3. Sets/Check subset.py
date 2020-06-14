for i in range(int(input())):
    x = input() 
    a=set(input().split())
    y=input()
    b=set(input().split())
    print(a.issubset(b))