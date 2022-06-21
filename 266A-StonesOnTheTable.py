n=int(input())
l=input()
cnt=0
for i in range(0,n-1):
    if(l[i]==l[i+1]):
        cnt+=1
print(cnt)
