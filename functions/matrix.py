def matrix():
    a = [i for i in range(6)]
    b = [a.copy() for j in range(6)]
    return b
def printmatrix(matrix):
    maxy = len(matrix)
    maxx = len(matrix[0])
    for i in range(maxy):
        for j in range(maxx):
            print('\t', matrix[i][j], end="")
        print()
#b=printmatrix(matrix())

def sum(a,y,x,dy,dx):
    maxx=len(a)
    # print(y,x,dy,dx)
    if dy>maxx:
        return "None"
    if dx>maxx:
        return "None"
    total=0
    for i in range(y,y+ dy):
        for j in range(x,x+dx):
            total+=a[i][j]
            print(a[i][j],end="\t")
        print()
    return "total=",total
a=matrix()
printmatrix(a)
print(sum(a,1,1,3,3))
maxsum=sum(a,0,0,3,3)
for i in range(7-3):
    for j in range(7-3):
        x=sum(a,i,j,3,3)
        if x>maxsum:
            maxsum=x
print("max:" , maxsum)