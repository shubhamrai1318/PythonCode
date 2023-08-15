def array():
    # a=["A","B","C","D","E"]
    inf=float("inf")
    l=[[" ","A","B","C","D","E"],["A",0,10,inf,5,inf],["B",inf,0,inf,2,100],["C",inf,0,inf,2,inf],["D",2,3,9,0,2],["E",7,inf,6,7,0]]
    return l
def printArray(array):
    for i in range(len(array)):
        for j in range(len(array)):
            print('\t\t\t'+ str(array[i][j]),end="")
        print()
def min(x,y):
    if x<=y:
        return x
    else:
        return y
def searchElement(array):
    min=array[1][2]
    n=len(array)
    for i in range(2,n):
        if array[1][i]<min:
            min=array[1][i]
            min_pos=i
    print("\nmin=",min,"\npos=",min_pos)
    # for i in range(2,n):
    #     array[1][i]=min(array[0][i],array[0][min_pos]+array[min_pos][i])
a=printArray(array())
b=searchElement(array())
