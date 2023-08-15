def SelectionSort(l):
    n = len(l)
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


l = [7, 2, 4, 9, 6]
SelectionSort(l)
print(l)
a = [2, 4, 1, 33, 2]
SelectionSort(a)
print(a)
