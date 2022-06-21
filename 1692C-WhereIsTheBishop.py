for i in range(int(input())):
    input()
    l=[input() for i in range(8)]
    cnt=[i.count("#") for i in l]
    i=1
    while(i<7):
        if(cnt[i-1]==2 and cnt[i]==1 and cnt[i+1]==2):
            break
        i+=1
    print(i+1,l[i].index("#")+1)
