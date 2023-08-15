n=10
for i in range(1,n+1):
    for j in range(1,n+1):
        l=[j*i]
        print(l,end="")
    print()
print("\n")
#fibonacci series with list

n=10
a=0
b=1
l=[0,1]
i=3
for i in range(3,n+1):
    c=a+b
    l=l + [c]
    a=b
    b=c
    i+=1
print(l,end="")