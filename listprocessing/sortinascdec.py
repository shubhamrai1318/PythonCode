"""m=input()
n=m.split(" ")
"""
a=input()
x=a.split(" ")
lenx=len(x)
b=input()
y=b.split(" ")
for i in x:
    x1=int(i)
    print(type(i))

# print(m,x,y,lenx)
for i in range(lenx-1):
    for j in range(lenx-i-1):
        if int(x[j])<=int(x[j+1]):
            continue
        t=int(x[j])
        int(x[j])=int(x[j])
print(x)
leny=len(y)
for i in range(leny):
    y.sort()
print(x+y)
