l = [5,4,3,2,1]
pos = 1
pos -= 1
left = 0
right = len(l) - 1

while True:
    pivot = l[left]
    fp = left
    for i in range(left + 1, right + 1):
        if l[i] >= pivot:
            continue
        fp = fp + 1
        l[i], l[fp] = l[fp], l[i]
    l[left], l[fp] = l[fp], l[left]
    if fp == pos:
        print("Found ", pivot)
        break
    if pos < fp:
        right = fp - 1
    else:
        left = fp + 1
print(l)
