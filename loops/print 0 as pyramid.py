n=4
for i in range(1,n+1):
    print("0",end="")
for row in range(1,n):
    for zero in range(1,n-row +1):
        print("0",end="")
    for space in range(1,2*row):
        print("-",end="")
    for zero2 in range(1,n-row+1):
        print("0",end="")
    print()
