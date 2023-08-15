l=[2,3,5,7,11,15,2,17,21,22,8,9,29,31]
n=len(l)
last=l[n-1]
last=last-1
l=l + [last]
print(l)
n=len(l)
p1=0
for i in range(n-1):
    if l[i]>l[i+1]:
        p2=i
        part=l[p1:p2+1]
        print(part,end="")
        print(p1,p2,end="")
        p1=p2+1

