l = [7, 2, 4, 9, 6]
n = len(l)
print("Input Array")
print(l)
for i in range(n - 1):
    min = l[i]
    pos = i
    for j in range(i + 1, n):
        if l[j] < min:
            min = l[j]
            pos = j
    t = l[i]
    l[i] = l[pos]
    l[pos] = t
    print("Array after {0} loop ".format(i + 1))
    print(l)

print("Sorted Array")
print(l)

"""
a=2
b=3
t=a  a=2,b=3, t=2
a=b  a=3, b=3, t=2
b=t   a=3,b=2,t=2

"""
