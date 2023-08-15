"""a=[1,2,3,4]
k=len(a)
b = ((x, y) for x in a for y in a if x!=y and x<y)
for element in b:
    print(element)

for i in range(1,4):
    for j in range(1,4):
        for k in range(1,4):
            if i!=j and i!=k and j!=k:
                print(i,j,k)

a=["A","B","C"]
for i in range(1,4):
    for j in range(1,4):
        for k in range(1,4):
            if i!=j and i!=k and j!=k:
                print(a[i-1],a[j-1],a[k-1])
"""


