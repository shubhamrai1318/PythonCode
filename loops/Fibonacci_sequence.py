n=10

a=0
b=1
print(a,"\t",b,"\t",sep=",",end=",")
i=3
while i<=n:
    c=a+b
    print(a,"+",b,"=",c,"\t" ,end=",\t")
    a=b
    b=c
    i+=1



