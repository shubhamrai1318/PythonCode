n=5
for row in reversed(range(1,n+1)):
    for zero in reversed(range(1,row+1)):
        print("0",end="")
    for space in reversed(range(1,n-row+1)):
        print("  ",end="")
    for zero in reversed(range(1,row+1)):
        print("0",end="")
    print()
