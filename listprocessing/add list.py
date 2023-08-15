# Partitioning the list

l = [10, 17, 3, 15, 8]
pivot = l[0]
fp = 0
n = len(l)
for i in range(n):
    if l[i] >= pivot:
        continue
    else:
        fp = fp + 1
        l[i], l[fp] = l[fp], l[i]
l[0], l[fp] = l[fp], l[0]
print(l)

# sorting the list with quick sort

def quickSort(l, left, right):
    if left >= right:
        return
    pivot = l[left]
    fp = left
    for i in range(left + 1, right + 1):
        if l[i] >= pivot:
            continue
        else:
            fp = fp + 1
            l[i], l[fp] = l[fp], l[i]
    l[left], l[fp] = l[fp], l[left]
    quickSort(l, left, fp - 1)
    quickSort(l, fp + 1, right)

quickSort(l, 0, n - 1)
print(l)
