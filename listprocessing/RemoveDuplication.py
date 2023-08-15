n = input()
m = int(n)
a = []
while m > 0:
    x = m % 10
    m = m // 10
    a = [x] + a
print(a)
noduplicate = []
l = len(a)
a = a + [a[l - 1] + 1]
p1 = 0
for i in range(1, l + 1):
    if a[i] == a[i - 1]:
        continue
    p2 = i
    # print(a[p2])
    b = a[p1:p2]
    if len(b) == 1:
        noduplicate = noduplicate + [b[0]]
    p1 = p2
st=""
for i in noduplicate:
    st=st + str(i)
print(st)