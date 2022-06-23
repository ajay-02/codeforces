n=int(input())
l=list(map(int,input().split()))
s=[0]*n
for x in range(1,n+1):
    s[l[x-1]-1]=x
print(*s)
