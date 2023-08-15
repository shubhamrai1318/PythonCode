n=5
for row in range(1,n+1):
    for space in range(1,n-row + 1):
        print(" ",end="")
    for star in range(1,row+1):
        ch=ord('A') + star -1
    for star in reversed (range(1, row)):
        ch=ord('A') + star-1
        print(chr(ch), end="")
    print()
