n=10
mid = (n+1)/2
for row in range(1,n+1):
    for column in range(1,n+1):
        condition = row + column == n+1 or row==column
        if condition:
            print("0",end="")
        else:
            print(" ",end="")
    print()

n=7
mid = (n+1)/2
for row in range(1,n+1):
    for column in range(1,n+1):
        condition = row==mid or column ==mid or row+column==5 or row+column==11 or row+column==mid+2
        if condition:
            print("*",end="")
        else:
            print(" ",end="")
    print()
