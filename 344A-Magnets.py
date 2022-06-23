l=[]
g=1
n=int(input())
l.append(input())
for i in range(n-1):
    x=input()
    if(l[-1]!=x):
        g+=1
    l.append(x)
print(g)
