def num_handshakes(n):
    if n % 2 == 1:
        return 0
    elif n == 0:
        return 1
    res = 0
    for i in range(0, n, 2):
        res += num_handshakes(i) * num_handshakes(n-2-i)
    return res
a=num_handshakes(8)
print(a)
