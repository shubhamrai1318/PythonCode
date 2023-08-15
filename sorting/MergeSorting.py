def mergeSort(a, left, right):
    if left >= right:
        return
    mid = (left + right) // 2
    print(left,right,mid)
    # print(a[left:right + 1])
    mergeSort(a, left, mid)
    mergeSort(a, mid + 1, right)
    # a1=left to mid, mid +1 to right
    c = []
    i = left
    j = mid + 1
    # Both array have elements
    while i <= mid and j <= right:
        if a[i] <= a[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(a[j])
            j += 1
    #  Check for remaining array
    if i <= mid:
        c = c + a[i:mid + 1]
    else:
        c = c + a[j:right + 1]
    # Transfer back
    n = len(c)
    for k in range(n):
        a[left + k] = c[k]
l = [2, 1, 3, 5, 4]
print(l)
n = len(l)
mergeSort(l, 0, n - 1)
print(l)
