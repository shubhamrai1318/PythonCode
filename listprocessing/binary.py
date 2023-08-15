n = 27
s = ""
aord = ord('A')
while (n != 0):
    rem = n % 26
    if rem == 0:
        n = n - 1
        rem = 1
    ch = chr(aord + rem - 1)
    s = str(ch) + s
    n = n // 26
print(s)

