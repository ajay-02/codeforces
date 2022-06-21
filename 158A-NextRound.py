n,k=map(int,input().split())
l=list(map(int,input().split()))
print(len([i for i in l if(i!=0 and i>=l[k-1])]))
