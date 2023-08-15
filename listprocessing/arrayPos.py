n=int(input())
l= input()
l=l.split(" ")
minpos=0
maxpos=0

for pos in range(n):
    if l[pos]<l[minpos]:
        minpos=pos
    elif l[pos]>l[maxpos]:
        maxpos=pos
print(minpos,maxpos,maxpos-minpos)