l = [7, 2, 4, 9, 6]
n = len(l)
print("Input Array")
print(l)
for i in range(n-1):
    for j in range(n-1-i):
        if l[j]<=l[j+1]:
            continue
        t=l[j]
        l[j]=l[j+1]
        l[j+1]=t
        print(l)
print("Sorted Array")
print(l)

