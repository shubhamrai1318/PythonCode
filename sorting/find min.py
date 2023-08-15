l = [7, 2, 4, 9, 6]
n = len(l)
min = l[0]
pos = 0
for i in range(1, n):
    if l[i] < min:
        min = l[i]
        pos = i
print(pos, min)
