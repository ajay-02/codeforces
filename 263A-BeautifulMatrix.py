x,y=0,0
for i in range(5):
    s=input().split()
    if('1' in s):
        x=i
        y=s.index('1')
print(abs(x-2)+abs(y-2))
