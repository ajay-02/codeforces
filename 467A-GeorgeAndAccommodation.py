cnt=0
for i in range(int(input())):
    n,m=map(int,input().split())
    if(m-n>=2):
        cnt+=1
print(cnt)
