n,s=int(input()),input()
a=sum([1 for i in s if(i=="A")])
d=sum([1 for i in s if(i=="D")])
if(a-d==0):
    print("Friendship")
elif(a-d>0):
    print("Anton")
else:
    print("Danik")
