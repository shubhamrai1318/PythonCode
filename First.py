a = [1, 3, 4, 5, 6, 7, 8, 9]
b = [2, 4, 5, 6, 7, 8, 9, 10]
c = []
n1 = len(a)
n2 = len(b)
i = 0
j = 0
while i <= n1 - 1 and j <= n2 - 1:
    if a[i] <= b[j]:
        c = c + [a[i]]
        i += 1
    else:
        c = c + [b[j]]
        j += 1

if i <= n1 - 1:
    c = c + a[i:]
else:
    c = c + b[j:]
print(c)
