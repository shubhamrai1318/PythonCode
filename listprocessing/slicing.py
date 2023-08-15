l=[4,2,4,5,23,54,34,65,2,3,4,56,23]
print(l)
n=len(l)
print("length of list:",n)
max=l[0]
pos_min=0
pos_max=0
min=l[0]
for i in range(1,n):
    if l[i]>max:
        pos_max=i
        max=l[i]
    elif l[i]<min:
        pos_min=i
        min=l[i]
print("min:",min,"pos_min:",pos_min,"\nmax:",max,"pos_max:",pos_max)
l.sort()
print("elements in assending order:",l)
l.sort(reverse=True)
print("elements in desending order:",l)
