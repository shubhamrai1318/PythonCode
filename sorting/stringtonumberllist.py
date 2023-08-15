def strtoarray():
    x = input()
    x = x.split(" ")
    # print(x)
    n = len(x)
    for i in range(n):
        x[i] = int(x[i])
    # print(  x)
    return x


def doTheSort(a, direction):
    if direction == 0:
        return sorting(a)
    else:
        return revsorting(a)


def sorting(a):
    lena = len(a)
    for i in range(lena - 1):
        for j in range(lena - 1 - i):
            if a[j] <= a[j + 1]:
                continue
            t = a[j]
            a[j] = a[j + 1]
            a[j + 1] = t
    return a


def revsorting(a):
    lena = len(a)
    for i in range(lena - 1):
        for j in range(lena - 1 - i):
            if a[j] >= a[j + 1]:
                continue
             t = a[j]
            a[j] = a[j + 1]
            a[j + 1] = t
    return a
def arraytostr(c):
    st=""
    for i in c:
        st=st+str(i)+" "
    return st


m=strtoarray()
a = strtoarray()
b = strtoarray()
# print(a, b, lena)
x = sorting(a)
y = revsorting(b)
c=x+y
# print(c)
r=arraytostr(c)
print(r)