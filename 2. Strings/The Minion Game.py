def minion_game(Str):
    Stuart=0
    Kevin=0
    for i in range(len(Str)):
        if Str[i]=='A'or Str[i]=='E'or Str[i]=='I'or Str[i]=='O' or Str[i]=='U':
            Kevin+=len(Str)-i
        else:
            Stuart+=len(Str)-i
    if Stuart==Kevin:
        print("Draw")
    elif Kevin>Stuart:
        print("Kevin "+str(Kevin))
    else:
        print("Stuart "+str(Stuart))
    

if __name__ == '__main__':
    s = input()
    minion_game(s