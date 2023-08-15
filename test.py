def pyramid():
    l=2
    for i in range(l):
        n = 8
        if i!=l:
            for row in range(1,n+1):
                for space in range(1,n-row + 1):
                    print(" ",end=" ")
                for star in range(1,2*row):
                    print("*",end=" ")
                for space in range(1,2*(n-row +1)):
                    print("#",end=" ")
                print("0")
        else:
            print("abc")





a=pyramid()
