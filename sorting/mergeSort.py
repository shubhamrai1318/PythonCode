a=[3,4,7,9,11,45,67]
b=[2,4,5,10]
c=[]
m=len(a)
n=len(b)
i=0
j=0
while i<=m-1 and j<=n-1:
    if a[i]<=b[j]:
        c.append(a[i])
        i+=1
    else:
        c.append(b[j])
        j+=1
if i!=m-1:
    c.append(b[j])
else:
    c.append(a[i])
print(c)