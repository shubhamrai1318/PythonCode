def quickSort(a, left, right):
    if left >= right:
        return
    pivot = a[left]
    fp = left
    # print(a)
    for i in range(left + 1, right + 1):
        if a[i] >= pivot:
            continue
        else:
            fp = fp + 1
            a[i], a[fp] = a[fp], a[i]
    a[left], a[fp] = a[fp], a[left]
    quickSort(a, left, fp - 1)
    quickSort(a, fp + 1, right)


a = [10,17,3,15,8]
n = len(a)
quickSort(a, 0, n - 1)
print(a)
