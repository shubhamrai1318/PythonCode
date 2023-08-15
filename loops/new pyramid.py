def pascal(y,x):
    if x==1:
        return 1
    if y==x:
        return 1
    return pascal(y-1,x) + pascal(y-1,x-1)
n=6
for row in range(1,n+1):
    for space in range(1,n-row+1):
        print("  ",end="")
    for zero in range(1,row+1):
        value=pascal(row,zero)
        print(value,"  ",end="")
    print()

