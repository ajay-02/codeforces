k,n,w=map(int,input().split())
x=sum([i*k for i in range(1,w+1)])
print(x-n if(x>=n) else 0)
