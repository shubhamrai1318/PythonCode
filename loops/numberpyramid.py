n=5
for row in range(1,n+1):
    for space in range(1,n-row + 1):
        print(" ",end="")
    for star in range(1,row+1):
        print(star,end="")

    for star in reversed (range(1, row)):
        print(star, end="")
    print()
