for i in range(int(input())):
    l=list(map(int,input().split()))
    print(len([i for i in l[1:] if(i>l[0])]))
