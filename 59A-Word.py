s=input()
if(sum([1 for i in s if(i.islower())])>=sum([1 for i in s if(i.isupper())])):
    print(s.lower())
else:
    print(s.upper())
