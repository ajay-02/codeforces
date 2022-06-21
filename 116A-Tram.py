m=0
c=0
for i in range(int(input())):
    ex,en=map(int,input().split())
    c-=ex
    c+=en
    m=max(m,c)
print(m)
