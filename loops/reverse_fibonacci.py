n=10
c=89
b=55
print(c,b,sep=",",end=",")
i=3
while i<=n:
    a=c-b
    print(a,end=",")
    c=b
    b=a
    i+=1
print(0)
